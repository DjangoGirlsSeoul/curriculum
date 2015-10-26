import sys
import string

class WordChainer(object):
    def __init__(self, start_word, end_word):
        with open('dictionary.txt') as f:
            self.dictionary  = set([line.rstrip() for line in f])
        self.start_word = start_word
        self.end_word = end_word
        self.current_words = [start_word]
        self.all_seen_words = {start_word: None}

    def adjacent_words(self, word):
        adjacent_words = []
        for i, letter in enumerate(word):
            for new_letter in list(string.ascii_lowercase):
                new_word = list(word)
                new_word[i] = new_letter
                new_word = "".join(new_word)
                if new_word in self.dictionary:
                    adjacent_words.append(new_word)
        return adjacent_words

    def run(self):
        while self.current_words:
            self.explore_current_words()
        return self.build_path(self.end_word)

    def explore_current_words(self):
        new_current_words = []
        for current_word in self.current_words:
            for adjacent_word in self.adjacent_words(current_word):
                if adjacent_word in self.all_seen_words:
                    continue
                new_current_words.append(adjacent_word)
                self.all_seen_words[adjacent_word] = current_word
        self.current_words = new_current_words

    def build_path(self, word):
        path = [word]
        while self.all_seen_words[word]:
            path.append(self.all_seen_words[word])
            word = self.all_seen_words[word]
        return path[::-1]


word_chainer = WordChainer(sys.argv[1], sys.argv[2])
path = word_chainer.run()
print(path)

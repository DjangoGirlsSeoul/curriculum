# Write a function that takes in a string. Your function should return the
# most common letter in the string, and a count of how many times it
# appears.
#
# Difficulty: medium.


def most_common_letter1(string):
    max_ch, max_count = '', 0

    for ch in string:
        count = string.count(ch)
        if count > max_count:
            max_ch, max_count = ch, count

    return [max_ch, count]


from collections import defaultdict
def most_common_letter2(string):
    count_dict = defaultdict(int, base=0)
    for ch in string:
        count_dict[ch] += 1

    reversed_count_dict = dict((v, k) for k, v in count_dict.items())
    max_count = max(reversed_count_dict.keys())

    return [reversed_count_dict[max_count], max_count]


def most_common_letter3(string):
    count_dict = {string.count(ch):ch for ch in string}
    max_count = max(count_dict.keys())
    return [count_dict[max_count], max_count]


def most_common_letter4(string):
    return max([[ch, string.count(ch)] for ch in string], key=lambda row: row[1])


# These are tests to check that your code is working. After writing
# your solution, they should all print true.

print('most_common_letter1("abca") == ["a", 2]: ' + str(most_common_letter1('abca') == ['a', 2]))
print('most_common_letter1("abbab") == ["b", 3]: ' + str(most_common_letter1('abbab') == ['b', 3]))

print('most_common_letter2("abca") == ["a", 2]: ' + str(most_common_letter2('abca') == ['a', 2]))
print('most_common_letter2("abbab") == ["b", 3]: ' + str(most_common_letter2('abbab') == ['b', 3]))

print('most_common_letter3("abca") == ["a", 2]: ' + str(most_common_letter3('abca') == ['a', 2]))
print('most_common_letter3("abbab") == ["b", 3]: ' + str(most_common_letter3('abbab') == ['b', 3]))

print('most_common_letter4("abca") == ["a", 2]: ' + str(most_common_letter4('abca') == ['a', 2]))
print('most_common_letter4("abbab") == ["b", 3]: ' + str(most_common_letter4('abbab') == ['b', 3]))


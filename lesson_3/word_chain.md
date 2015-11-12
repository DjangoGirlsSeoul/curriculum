# Word Chains
단어 사슬
** Review everything here before starting **
시작하기에 앞서 전체 내용을 먼저 읽어보세요.

Given two words of equal length as command-line arguments, 
build a chain of words connecting the first to the second. 
Each word in the chain must be in the dictionary and 
every step along the chain changes exactly one letter from the previous word.
command line의 argument와 동일한 길이의 두 단어를 부여하고,
첫 번째 단어를 두 번째 단어로 연결시키는 단어 사슬을 만들어 보세요.
사슬의 각 단어는 dictionary에 포함된 것이어야 하고,
각 단계는 이전 단어의 한 글자만을 변하게 해야 합니다.

```
python word_chain.py cat dog

cat, cot, dot, dog
```

## Phase I: Adjacent Words
1 단계 : 인접한 단어들

The dictionary is in the repo as `dictionary.txt'
dictionary는 repo에 있으며, 'dictionary.txt'입니다.

Let's write a class `WordChainer`.
Begin writing the `__init__(self, dictionary_file_name)` method. Read in
the dictionary file. Store the array of dictionary words in an
member variable (e.g., `self.dictionary`).
'WordChainer' class를 작성 해 봅시다.
'__init__(self, dictionary_file_name)' method를 쓰는 것으로 시작 해 봅시다. 
dictionary file을 읽어내도록 하세요.
dictionary에 배열된 단어들을 구성요소 변수 (member variable)로 저장하게 하세요. (예, 'self.dictionary')

Next, write a helper method `adjacent_words(word)`. This should
return all words in the dictionary one letter different than the
current word.
다음으로, helper method 'adjacent_words(word)'를 작성 해 보세요.
현재 단어에서 한글자가 다른 단어들을 이 method가 모두 return 하게 해야 합니다. 

Verify that your `adjacent_words` method is working.
'adjacent_words' method가 잘 작동하는지 확인 해 보세요.

## Phase IIa: Exploring all words
2a단계 : 모든 단어 탐색하기

Next, let's begin writing a method `run(source, target)`. Our
strategy is:
'run(source, target)' method를 작성하는 것으로 시작 해 봅시다. 우리의 전략은 이렇습니다. :

* Keep a list of `current_words`. Start this with just `[source]`.
'current_words' 목록을 유지합니다. '[source]'단어로 시작하도록 하세요..

* Also keep a list of `all_seen_words`. Start this with just
  `[source]`.
'all_seen_words' 목록 역시 유지합시다. '[source]'단어로 시작하도록 하세요.

* Begin an outer loop which will run as long as `current_words` is
  not empty.
'current_words'가 비어있지 않는한 계속 작동되는 outer loop를 시작 시키세요.

* The first thing to do in the inner loop is to create a new, empty
  list of `new_current_words`. We're going to fill this up with new
  words (that aren't in `all_seen_words`) that are adjacent (one step
  away) from a word in `current_words`.
inner loop에서 가장 먼저 해야 하는 것은, 새로운 'new_current_words' 빈 목록을 생성하는 것입니다.  
'current_words'에 있는 단어로부터 인접한 (한단계 변환된) 새로운 단어들('all_seen_words'에는 없는)로 빈 목록을 채울겁니다.

* To fill up new_current_words, begin an inner loop through
  `current_words`.
'new_current_words'를 채우기 위하여, 'current_words'로 inner loop를 작동 시키세요.

* For each `current_word`, iterate through all
  `adjacent_words(current_word)`. This is a triply nested loop.
각각의 'current_word'를 위해서, 모든 'adjacent_words(current_word)'를 반복하도록 하세요.
이것은 삼중으로 짜여진 loop입니다.

* For each `adjacent_word`, skip it if it's already in
  `all_seen_words`; we don't need to reconsider a word we've seen
  before.
각각의 'adjacent_word'가 'all_seen_words'에 이미 있는 단어라면 건너뛰게 하세요.
이전에 본 적이 있는 단어들을 또다시 살펴봐야 할 필요는 없습니다.

* Otherwise, if it's a new word, add it to both `new_current_words`,
  and `all_seen_words` so we don't repeat it.
그렇지 않고 만약 새로운 단어라면 'new_current_words'와 'all_seen_words'에 모두 추가 시켜서, 이제 반복되지 않게 만들어 주세요.

* After we finish looping through all the `current_words`, print out
  `new_current_words`, and reset `current_words` to
  `new_current_words`.
'current_words'의 모든 단어에 대해서 loop 작동이 끝나면, 'new_current_words'를 출력시키고,
'current_words'를 'new_current_words'로 reset 시키도록 하세요.

Test your word chainer to make sure it returns (1) first the words
that are one letter away from `source`, (2) next words that are one
letter away from words one letter away from `source` (i.e., two
letters away from source), etc. This is a **breadth first**
enumeration of words that you can reach from the `source`.
지금까지 만들어 본 단어사슬장치가 다음과 같이 작동하는지 확인 해 보세요.
(1) return 결과로 나온 첫 단어가 'source' 단어에서 한 글자 바뀐 단어이며
(2) 두 번째 return 결과로 나온 단어는 (1)에서 나온 단어에서 한 글자 바뀐 단어임
(예, source 단어에서 두 글자 바뀐 단어가 나옴)

Make sure your `run` method eventually terminates: it should
eventually enumerate all the words that are reachable from `source`,
at which point `new_current_words` will come out empty. After setting
`@current_words = new_current_words`. The outermost loop should
terminate.
'run' method가 결국에는 끝나지도록 하세요.: 
'new_current_words'가 더 이상 없는 상태로, 'source'로부터 만들어진 단어들이 결과적으로 나열되어야 합니다.
'@current_words = new_current_words'를 셋팅하고, outermost loop가 종료되도록 하세요.

**Call a coach over to check your work**.
잘 작동하는지 체크할때 코치를 불러주세용!

## Phase IIb: Refactor
2b 단계 : 코드 변형 

Your code will contain a triply nested loop. Break out the inner loop
that iterates through `current_words` and builds and assigns the
`new_current_words` to its own method: `explore_current_words`.
작성한 code는 삼중으로 짜여진 loop를 포함하게 될 것입니다.
inner loop를, 'current_words'로 계속 반복되면서도 inner loop 내부 method로써 'explore_current_words'가 작성되어 지정될 수 있도록 하세요.

## Phase III: Keep Track of Prior Words
3단계 : 이전 단어의 추적을 지속하기

So far we've written our program to build a set of `all_seen_words`,
adding new words in breadth-first order. However, we don't record
enough information to construct a path of words from the `source` to
the `target`.
새로운 단어를 펼쳐놓게 추가 함으로써 'all_seen_words'셋트를 만들기 위한 코드가 이제 어느정도 작성이 되었습니다.
하지만 'source'단어에서 'target'단어까지의 경로를 구성하기 위한 충분한 정보가 저장되어 있는 상태가 아직 아닙니다.

Let's change our program. For every new word we encounter, let's
record which previous word we modified to get to the new word. To do
this, instead of keeping an array of `all_seen_words`, lets make it a
hash, where the keys are new words, and the value is the word we
modified to get to the new word.
프로그래밍 한 것을 조금 바꿔봅시다.
새로 나오는 각각의 단어들이 전에 나왔던 어떤 단어를 변형했던 것인지 저장하도록 만들어 봅시다.
이렇게 진행하기 위해서 'all_seen_words'의 배열을 대신하여,
새로운 단어가 나온 부분의 key 값과, 새로운 단어를 얻기 위해서 변경한 단어의 value값으로 내용을 쪼개볼게요.

Let's start `all_seen_words` out as `{ source: None }`, since
`source` didn't come from anywhere. Let's modify
`explore_current_words` so that instead of merely adding an
`adjacent_word` to the array, we record it as the key, where the value
is the `current_word` we came from.
'source'단어가 어느곳에서도 나온 것이 아니므로, 'all_seen_words'를 '{ source: None }'으로 지정하세요.
'adjacent_word'가 배열에 단순하게 추가되는 것을, 'explore_current_words'가 대신하도록 변형해 봅시다. 
변형을 시작했던 'current_word'에서 value가 있는 곳이 key 값으로 저장되게 하세요.

Modify `explore_current_words` to print not just the new words, but
where they came from. At the end of `explore_current_words`, iterate
through `new_current_words`, and print out the new word and the word
it came from (the value in the `all_seen_words` dictionary). Make sure this
output makes sense. You may want to use a longer word like `"market"`
to reduce the verbosity of the output.
생성된 새로운 단어 뿐만 아니라 그 출처도 함께 print 되도록 'explore_current_words'를 변형 해 볼게요.
'explore_current_words' 마지막 부분에 'new_current_words'를 반복 시키고,
새로운 단어와 그 출처가 되는 단어 ('all_seen_words' dictionary의 value 값)가 print 되도록 하세요.
output이 뜻이 있는 말이 되도록 만드세요. output으로 나오는 양을 줄이려고 아마 'market'같은 긴 단어를 사용하고 싶어 할지도 모르겠네요.

**Check with a coach after this phase.**
이 단계를 마쳤으면 코치에게 확인 받으세요. (짝짝짝!!)

## Phase IV: Backtracking
4단계 : 역추적하기

Okay! Right now `run` builds `all_seen_words`, but it never
constructs the path from the source to the target. Let's use
`all_seen_words` to do this.
자, 지금 'run'이 'all_seen_words'를 만들지만, source에서 target으로 보내는 경로를 구성하지는 않습니다.
'all_seen_words'를 사용해서 경로를 만들어 봅시다.

Write a method named `build_path(target)`. It should look up the
target in `all_seen_words`. This is the word we were at before the
final step to `target`. Then we need to look up the word we used to
get the second to last word. Then the word before that.
'build_path(target)'으로 이름붙인 method를 작성 해 보세요.
'all_seen_words'안에 target 단어가 있는지 살펴보게 해야 합니다.
이 단어가 'target'단어가 나오기 직전에 마지막으로 나왔던 단어입니다.
그리고 나서 마지막으로 나온 단어의 두 단계 전에 나왔던 단어를 살펴보고,
그 다음에 그 단어의 이전 단계에 나왔던 단어를 살펴보게 하세요.

Keep looking back and back in from `target` in
`all_seen_words`. Each time, add the prior word to an array named
`path`. Eventually you will reach `None`, which means we've reached the
end of the path back to `source`.
'all_seen_words'에서 어떤 단어들이 'target' 단어까지로 변환된 것인지 'target'단어부터 계속 되짚어 보게 하세요.
'path'로 이름붙인 배열에 이전에 나온 단어를 매 번 추가하세요.

Have `run` call `build_path` and return the array.
'run'이 'build_path'를 호출하도록 하고, 배열을 return으로 받으세요.

**Make sure to request a code review from your coach once you can find
adjacent words**.
인접한(변형된) 단어가 나오면 코치에게 작성한 코드를 확인 받으세요~

## Bonus Phase: Stop Early
뽀너스: 조기 종료 시키기

Your `run` method will build the entire set of reachable words. This
is wasteful if the source is close to the target. We can stop early in
that case. Modify `run` to stop looping when `all_seen_words`
contains the target.
'run' method는 변형 가능한 단어의 전체 세트를 만들어 낼 것입니다.
만약 source가 target에 이미 가까워 졌다면 계속할 필요가 없겠지요.
이런 경우에 우리는 진행을 종료시킬 수 있습니다.
'all_seen_words'가 target 단어를 포함하게 되면 loop를 종료할 수 있도록 'run' method를 변형 해 보세요.

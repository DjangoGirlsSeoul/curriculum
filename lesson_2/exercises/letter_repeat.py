# Write a function that takes in a string and returns the number of
# letters that appear more than once in the string.
# string에서 한 번 이상 나오는 글자의 갯수를 나오게 하는 함수를 입력하세요.
# The string will contain only lowercase letters. Count the number of
# letters that repeat, not the number of times they repeat in the
# string.
# string은 소문자만 표시할 것입니다. 반복되는 글자의 수를 세어보세요, 반복되는 횟수를 세는 것은 아닙니다.
# 
# Difficulty: hard.
# 난이도: 상

def num_repeats(string):
    return "hi"

# These are tests to check that your code is working. After writing
# your solution, they should all print true.

print('num_repeats("abdbc") == 1: ' + str(num_repeats('abdbc') == 1))
# one character is repeated
print('num_repeats("aaa") == 1: ' + str(num_repeats('aaa') == 1))
print('num_repeats("abab") == 2: ' + str(num_repeats('abab') == 2))
print('num_repeats("cadac") == 2: ' + str(num_repeats('cadac') == 2))
print('num_repeats("abcde") == 0: ' + str(num_repeats('abcde') == 0))

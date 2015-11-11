# Write a function that takes in a string and returns the number of
# letters that appear more than once in the string.
# The string will contain only lowercase letters. Count the number of
# letters that repeat, not the number of times they repeat in the
# string.
#
# Difficulty: hard.


def num_repeats1(string):
    count_dict = {ch: string.count(ch) for ch in string}
    return len([ch for ch, count in count_dict.items() if count > 1])


from collections import defaultdict
def num_repeats2(string):
    count_dict = defaultdict(int, base=0)
    for ch in string:
        count_dict[ch] += 1

    return len([ch for ch, count in count_dict.items() if count > 1])


from itertools import groupby
def num_repeats3(string):
    count = 0
    for key, group in groupby(sorted(list(string))):
        if len(tuple(group)) > 1:
            count += 1
    return count


# These are tests to check that your code is working. After writing
# your solution, they should all print true.

print('num_repeats1("abdbc") == 1: ' + str(num_repeats1('abdbc') == 1))
print('num_repeats1("aaa") == 1: ' + str(num_repeats1('aaa') == 1))
print('num_repeats1("abab") == 2: ' + str(num_repeats1('abab') == 2))
print('num_repeats1("cadac") == 2: ' + str(num_repeats1('cadac') == 2))
print('num_repeats1("abcde") == 0: ' + str(num_repeats1('abcde') == 0))
print('')

print('num_repeats2("abdbc") == 1: ' + str(num_repeats2('abdbc') == 1))
print('num_repeats2("aaa") == 1: ' + str(num_repeats2('aaa') == 1))
print('num_repeats2("abab") == 2: ' + str(num_repeats2('abab') == 2))
print('num_repeats2("cadac") == 2: ' + str(num_repeats2('cadac') == 2))
print('num_repeats2("abcde") == 0: ' + str(num_repeats2('abcde') == 0))
print('')

print('num_repeats3("abdbc") == 1: ' + str(num_repeats3('abdbc') == 1))
print('num_repeats3("aaa") == 1: ' + str(num_repeats3('aaa') == 1))
print('num_repeats3("abab") == 2: ' + str(num_repeats3('abab') == 2))
print('num_repeats3("cadac") == 2: ' + str(num_repeats3('cadac') == 2))
print('num_repeats3("abcde") == 0: ' + str(num_repeats3('abcde') == 0))


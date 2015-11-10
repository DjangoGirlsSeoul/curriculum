# Write a function that takes in a string. Your function should return the
# most common letter in the string, and a count of how many times it
# appears.
# string을 가져오는 함수를 입력하세요. 그 함수는 string에서 가장 많이 나타나는 글자를 가져오고, 같은 글자가 몇 번 씩 나타나는지 셉니다.
#
# Difficulty: medium.
# 난이도: 중

def most_common_letter(string):
	common = dict()
	letters = list()
	for letter in string:
	    letters.append(letter)
	for x in letters:
		common[x] = common.get(x,0) + 1

	maxkey = 0
	maxval = 0
	for key,val in common.items():
	    if val > maxval:
	        maxkey = key
	        maxval = val

	return [maxkey, maxval]





# These are tests to check that your code is working. After writing
# your solution, they should all print true.

print('most_common_letter("abca") == ["a", 2]: ' + str(most_common_letter('abca') == ['a', 2]))

print('most_common_letter("abbab") == ["b", 3]: ' + str(most_common_letter('abbab') == ['b', 3]))

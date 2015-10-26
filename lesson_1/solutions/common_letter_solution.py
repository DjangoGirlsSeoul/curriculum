def most_common_letter(string):
	common = dict()
	letters = list()
	for letter in string:
	    letters.append(letter)
	for x in letters:
		common[x] = common.get(x,0) + 1

	maxkey = None
	maxval = None
	for key,val in common.items():
	    if val > maxval:
	        maxkey = key
	        maxval = val

	return maxkey, maxval





# These are tests to check that your code is working. After writing
# your solution, they should all print true.

print('most_common_letter("abca") == ["a", 2]: ' + str(most_common_letter('abca') == ['a', 2]))

print('most_common_letter("abbab") == ["b", 3]: ' + str(most_common_letter('abbab') == ['b', 3]))

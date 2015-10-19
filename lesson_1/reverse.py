# Write a function that takes in a string and returns a new
# string with the letters in reverse order. Assume that the input will always be strings.
#
# Difficulty: easy.

def reverse(string):
    # change the code below
    return string[::-1]


# These are tests to check that your code is working. After writing
# your solution, they should all print true. Do not change these

print('reverse("abc") == "cba": ' + str(reverse("abc") == "cba"))

print('reverse("a") == "a": ' + str(reverse("a") == "a"))

print('reverse("") == "": ' + str(reverse("") == ""))

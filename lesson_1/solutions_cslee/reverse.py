# Write a function that takes in a string and returns a new
# string with the letters in reverse order. Assume that the input will always be strings.
#
# Difficulty: easy.


def reverse1(string):
    letters = []
    for ch in string:
        letters.append(ch)
    letters.reverse()
    return ''.join(letters)


def reverse2(string):
    letters = []
    for ch in range(len(string)-1, -1, -1):
        letters.append(string[ch])
    return ''.join(letters)


def reverse3(string):
    letters = list(string)
    letters.reverse()
    return ''.join(letters)


def reverse4(string):
    return ''.join(reversed(string))


def reverse5(string):
    return string[::-1]


# These are tests to check that your code is working. After writing
# your solution, they should all print true. Do not change these

print('reverse1("abc") == "cba": ' + str(reverse1("abc") == "cba"))
print('reverse1("a") == "a": ' + str(reverse1("a") == "a"))
print('reverse1("") == "": ' + str(reverse1("") == ""))

print('reverse2("abc") == "cba": ' + str(reverse2("abc") == "cba"))
print('reverse2("a") == "a": ' + str(reverse2("a") == "a"))
print('reverse2("") == "": ' + str(reverse2("") == ""))

print('reverse3("abc") == "cba": ' + str(reverse3("abc") == "cba"))
print('reverse3("a") == "a": ' + str(reverse3("a") == "a"))
print('reverse3("") == "": ' + str(reverse3("") == ""))

print('reverse4("abc") == "cba": ' + str(reverse4("abc") == "cba"))
print('reverse4("a") == "a": ' + str(reverse4("a") == "a"))
print('reverse4("") == "": ' + str(reverse4("") == ""))

print('reverse5("abc") == "cba": ' + str(reverse5("abc") == "cba"))
print('reverse5("a") == "a": ' + str(reverse5("a") == "a"))
print('reverse5("") == "": ' + str(reverse5("") == ""))

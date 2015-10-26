# Write a function that takes in a string and returns a new
# string with the letters in reverse order. Assume that the input will always be strings.
#
# Difficulty: easy.
#Below are three examples of different solutions.  

def reverse(string):
    # change the code below
    return string[::-1]

def reverse2(string):
    letters = []
    for letter in string:
        letters.append(letter)
    letters.reverse()
    reverse = ''.join(letters)
    return reverse

def reverse3(string):
    #make an empty string
    revstring = ''
    #go through each letter of the string(for x) in range(start,stop,step)
    #len(string) - 1 is the start (so starting from the end of the string
    # stop at -1 (it will run up to but not including -1 so it will go until 0
    #step is -1 so it will go through the string 1 letter at a time but backwards
    for x in range(len(string)-1,-1,-1):
        revstring += string[x]
    return revstring

# These are tests to check that your code is working. After writing
# your solution, they should all print true. Do not change these

print('reverse("abc") == "cba": ' + str(reverse("abc") == "cba"))

print('reverse("a") == "a": ' + str(reverse("a") == "a"))

print('reverse("") == "": ' + str(reverse("") == ""))

# These are tests to check that your code is working. After writing
# your solution, they should all print true. Do not change these

print('reverse("abc") == "cba": ' + str(reverse("abc") == "cba"))

print('reverse("a") == "a": ' + str(reverse("a") == "a"))

print('reverse("") == "": ' + str(reverse("") == ""))

# These are tests to check that your code is working. After writing
# your solution, they should all print true. Do not change these

print('reverse("abc") == "cba": ' + str(reverse("abc") == "cba"))

print('reverse("a") == "a": ' + str(reverse("a") == "a"))

print('reverse("") == "": ' + str(reverse("") == ""))

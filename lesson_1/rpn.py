# # RPN Calculator
#
# "RPN" stands for "Reverse Polish Notation". (See [the wikipedia
# entry](http://en.wikipedia.org/wiki/Reverse_Polish_notation) for
# more information on this colorful term.) Briefly, in an RPN world,
# instead of using normal "infix" notation, e.g.
#
#     2 + 2
#
# you use "postfix" notation, e.g.
#
#     2 2 +
#
# While this may seem bizarre, there are some advantages to doing
# things this way. For one, you never need to use parentheses, since
# there is never any ambiguity as to what order to perform operations
# in. The rule is, you always go from the back, or the left side.
#
#     1 + 2 * 3 =>
#     (1 + 2) * 3 or
#     1 + (2 * 3)
#
#     1 2 + 3 * => (1 + 2) * 3
#     1 2 3 * + => 1 + (2 * 3)
#
# Another advantage is that you can represent any mathematical formula
# using a simple and elegant data structure, called a
# [stack](http://en.wikipedia.org/wiki/Stack_(data_structure)).
#
# # Hints
#
# Use python's lists for this exercise. The `append` and `pop` functions
# should help you out.
# 
# Also use the operator library `import operator`. This allows you to use 
# standard operators as functions. For example `operator.add(2,3)` returns `5`
# We have provided you with a dictionary of the valid operators.
#
# See
# * <http://en.wikipedia.org/wiki/Reverse_Polish_notation>
# * <http://www.calculator.org/rpn.aspx>

import operator

operators = {'+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
}

def rpn(input):
    # code here!


print('rpn("1 2 + 3 *") == 9: ' + str(rpn("1 2 + 3 *") == 9))

print('rpn("1 2 3 * +") == 7: ' + str(rpn("1 2 3 * +") == 7))

print('rpn("20 10 5 4 + * -") == -70: ' + str(rpn("20 10 5 4 + * -") == -70))

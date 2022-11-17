"""
lambda arg1, arg2, argN : expression
lambda is a expression, not a statement
expression: express a object, such as x+2, x**2
statement: complete some function,such as x=1,print(x),if x < 0.
"""

square = lambda x: x ** 2


def square2(x):
    return x ** 2
#
print(square(4))
print(square(100))
#
print(square2(4))

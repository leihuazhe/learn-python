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

# 在列表内部使用,def不能
print([(lambda x: x * x)(x) for x in range(10)])
# lambda 可以被用作某些函数的参数，而常规函数 def 也不能
l = [(1, 20), (3, 0), (9, 10), (2, -1)]
l.sort(key=lambda x: x[1])
print(l)
# 常规函数 def 必须通过其函数名被调用，因此必须首先被定义。
# 但是作为一个表达式的 lambda，返回的函数对象就不需要名字了。


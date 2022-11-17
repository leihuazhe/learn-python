"""
type 可以返回一个对象的类型. 通过 type 生成类,在元编程讲解.
a=1,1的type类型是 class 'int'.
class 也是一个对象, int class 的 type 类型是 class 'type'.

type -> int -> 1
type -> class -> object: type 生成 class, class 生成 object
object 是最顶层的基础类
type 也是一个类, 同时 type 也
type 与 object 的关系




list 是类
list 是对象,是 type 的对象.

一切皆对象,一切继承 object
"""

# type object class 区别
a = 1
b = "abc"
print(type(1))  # <class 'int'>
print(type(int))
print(type(b))  # <class 'str'>
print(type(str))  # <class 'type'>


class Student:
    pass


# 对象由类创建,类由 type 创建
stu = Student()
type(stu)  # <class '__main__.Student'>
type(Student)  # <class 'type'>

Student.__base__  # (<class 'object'>,)


class MyStudent(Student):
    pass


# (<class '__main__.Student'>,)
MyStudent.__bases__

type.__bases__  # (<class 'object'>,)
object.__bases__  # ()
type(object)  # <class 'type'>

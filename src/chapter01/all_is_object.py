def ask(name='bobby'):
    print(name)


class Person:
    def __init__(self):
        print('person')


my_func = ask
my_func('maple')

my_class = Person
my_class()

obj_list = []
obj_list.append(ask)
obj_list.append(Person)

for item in obj_list:
    print('item print:', item())


# 可以作为参数传递给函数
# 可以当作函数的返回值
def decorate_func():
    print('start')
    return ask

my_ask = decorate_func()
my_ask()
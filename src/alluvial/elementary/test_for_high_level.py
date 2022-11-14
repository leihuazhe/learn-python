import threading
import unittest

names = ['maple', 'ray', 'may', 'yang']

# expression1 if condition else expression2 for item in iterable
value = [item if item == 'maple' else item + 'else' for item in names]
print('value:', value)

# 2
x = [-2, -1, 0, 1, 2, 3, 4]
y = [value * 2 + 5 if value > 0 else -value * 2 + 5 for value in x]

print(y)

# 有 else 和没有 else 的写法
# expression1 if condition else expression2 for item in iterable
# expression for item in iterable if condition


# 文件处理
text = ' Today,  is, Sunday '
text_list = [s.strip() for s in text.split(',') if len(s.strip()) > 3]
text_list2 = [s.strip() for s in text.split(',')]
print(text_list)
print(text_list2)

xx = [1, 2, 3, 4, 5]
yy = [6, 7, 8, 9, 10]

res = [(x, y) for x in xx for y in yy if x != y]
print(res)

# 等价于
# l = []
# for x in xx:
#     for y in yy:
#         if x != y:
#             l.append((x, y))

# 最后给你留一个思考题。给定下面两个列表 attributes 和 values，要求针对 values 中每一组子列表 value，输出其和 attributes 中的键对应后的字典，最后返回字典组成的列表。


# expected outout:
# [{'name': 'jason', 'dob': '2000-01-01', 'gender': 'male'},
#  {'name': 'mike', 'dob': '1999-01-01', 'gender': 'male'},
#  {'name': 'nancy', 'dob': '2001-02-01', 'gender': 'female'}]
i = 3
i = i + 1

# , trailing commas 要换行,不能直接跟着 ) ] }.
FILES = [
    'setup.cfg',
    'tox.ini',
]


# l,O,I
def munge(input: bool) -> int:
    # threading.Thread
    return input.__hash__() + 2


def test_for_assignment():
    attributes = ['name', 'dob', 'gender']
    values = [
        ['jason', '2000-01-01', 'male'],
        ['mike', '1999-01-01', 'male'],
        ['nancy', '2001-02-01', 'female']
    ]
    # What is the zip used for?
    print([zip(attributes, value) for value in values])

    res = [dict(zip(attributes, value)) for value in values]
    print(res)


class TestDict(unittest.TestCase):
    def test_for_assignment(self):
        attributes = ['name', 'dob', 'gender']
        values = [
            ['jason', '2000-01-01', 'male'],
            ['mike', '1999-01-01', 'male'],
            ['nancy', '2001-02-01', 'female']
        ]
        res = [dict(zip(attributes, value)) for value in values]
        print(res)
        self.assertEquals(1, 1)


if __name__ == '__main__':
    unittest.main()

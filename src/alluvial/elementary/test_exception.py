# 捕获单个异常
import sys


def test_1():
    try:
        s = input('please enter two numbers separated by comma: ')
        num1 = int(s.split(",")[0].strip())
        num2 = int(s.split(",")[1].strip())
        print('num sum: {}'.format(num1 + num2))
    except ValueError as err:
        print('Value error: {}'.format(err))

    print('continue')


# 捕获多个异常
def test_2():
    try:
        s = input('please enter two numbers separated by comma: ')
        num1 = int(s.split(",")[0].strip())
        num2 = int(s.split(",")[1].strip())
        print('num sum: {}'.format(num1 + num2))
    except (IndexError, ValueError) as err:
        print('Value error: {}'.format(err))

    print('continue')


# 捕获多个异常,写法2
def test_3():
    try:
        s = input('please enter two numbers separated by comma: ')
        num1 = int(s.split(",")[0].strip())
        num2 = int(s.split(",")[1].strip())
        print('num sum: {}'.format(num1 + num2))
    except IndexError as err:
        print('Value error: {}'.format(err))
    except ValueError as err:
        print('Value error: {}'.format(err))
    # Exception 是其他所有非系统异常的基类，能够匹配任意非系统异常
    except Exception as err:
        print('Value error: {}'.format(err))
    # 省略异常类型，这表示与任意异常相匹配(包括系统异常)
    except:
        print('Other error')

    print('continue')


# finally
def test_finally():
    try:
        f = open('file.txt', 'r')
    except OSError as err:
        print('OS error: {}'.format(err))
    except:
        print('Unexpected error: ', sys.exc_info()[0])
    finally:
        f.close()


class MyInputError(Exception):
    """Exception raised when there've errors in input"""

    # 自定义异常类型的初始化
    def __init__(self, value):
        self.value = value

    def __str__(self):  # 自定义异常类型的 string 表达形式
        return ("{} is invalid input".format(repr(self.value)))


try:
    raise MyInputError(1)  # 抛出 MyInputError 这个异常
except MyInputError as err:
    print('error: {}'.format(err))

if __name__ == '__main__':
    test_1()
    test_2()

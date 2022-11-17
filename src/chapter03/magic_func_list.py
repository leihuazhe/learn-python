class Company(object):
    def __init__(self, employee):
        self.employee = employee

    def __str__(self):
        return ",".join(self.employee)

    # 在 python 命令行,或者 notebook 开发者模式进行调用
    def __repr__(self):
        return ",".join(self.employee)


company = Company(['tom', 'bob', 'jane'])
# 开发模式下,不需要显示的调用,interpretor 会 implicit call
company.__repr__()

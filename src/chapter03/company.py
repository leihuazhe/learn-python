# class Company(object):
#     def __init__(self, employee_list):
#         self.employee = employee_list
#
#     # 双下划线开头,双下划线结尾 属于 魔法函数
#     # 可以随意定义 company 的特性
#     def __getitem__(self, item):
#         return self.employee[item]
#
#     # def __iter__(self):
#     #     pass
#     # 可以直接让该类被len()
#     def __len__(self):
#         return len(self.employee)
#
#
# company = Company(["tom", "bob", "jane"])
# employee = company.employee
#
# # for em in employee:
# #     print(em)
#
# for c in company:
#     print(c)
#
# company1 = company[:2]
# for c in company1:
#     print(c)
#
# # object of type 'Company' has no len()
# print(len(company))

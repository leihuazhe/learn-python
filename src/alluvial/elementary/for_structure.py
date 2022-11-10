l = [1, 2, 3, 4]

for i in l:
    print(i)

# tabnine

i = 0
if i == 0:
    print(0)
elif i == 1:
    print(1)
else:
    print('unknown option')

d = {'name': 'jason', 'dob': '2000-01-01', 'gender': 'male'}

for key in d:
    print(key, d[key])

# ctrl alt v
for value in d.values():
    print(value)

for k, v in d.items():
    print(k, v)

l = [1, 2, 3, 4, 5, 6, 7]

for i in range(0, len(l)):
    print(l[i])

for index, item in enumerate(l):
    if index < 5:
        print(item)

# name_price: 产品名称 (str) 到价格 (int) 的映射字典
# name_color: 产品名字 (str) 到颜色 (list of str) 的映射字典

name_price = {'iphone': 6299, 'xiaomi': 3299, 'huawei': 4399}
name_color = {'iphone': ['green', 'white', 'blue'],
              'xiaomi': ['red', 'green', 'white', 'blue'],
              'huawei': ['red', 'green', 'white', 'blue']
              }

# 我们要找出价格小于 1000，并且颜色不是红色的所有产品名称和颜色的组合。如果不用 continue，代码应该是下面这样的：
for name, price in name_price.items():
    if price >= 5000:
        continue
    if name not in name_color:
        # print('name: {}, color: {}'.format(name, 'None'))
        continue
    for color in name_color[name]:
        if color == 'red':
            # print('name: {}, color: {}'.format(name, color))
            continue
        print('name: {}, color: {}'.format(name, color))

l = [1, 2, 3, 4]
index = 0
while index < len(l):
    print(l[index])
    index += 1

while True:
    try:
        text = input('Please enter your questions, enter "q" to exit')
        if text == 'q':
            print('Exit system')
            break
        print(text)
    except Exception as err:
        print('Encountered error: {}'.format(err))
        break

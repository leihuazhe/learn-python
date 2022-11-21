# 求平方根,保留6位小数
def square(n):
    low, high = 0, n
    cur_value = -1
    # 循环条件
    while high - low >= 0.00001:
        cur_value = low + (high - low) / 2
        if cur_value * cur_value < n:
            low = cur_value
        else:
            high = cur_value

    return format(cur_value, ".6f")


print(square(2))
print(square(4))


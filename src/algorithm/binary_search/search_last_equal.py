#
#
def binary_search(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            # 找符合最右边一个值得条件,返回,否则继续改变 bound
            # if mid == high or nums[mid + 1] != target:
            # 不能像上面这么写,因为 high 是一直在改变的,所以要修改为固定的 nums 长度 - 1
            if mid == len(nums) - 1 or nums[mid + 1] != target:
                return mid
            else:
                low = mid + 1
    return -1


print(binary_search([3, 4, 4, 4, 5, 6, 7, 8, 8, 9], 4))

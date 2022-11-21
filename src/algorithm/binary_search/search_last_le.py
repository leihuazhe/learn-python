#
# 查找最后一个小于或等于给定 target 的 index
# 1, 3, 5, 7 ,9
# target 6
# res = 5
# 终止条件、区间上下界更新方法、返回值选择
def binary_search(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if nums[mid] > target:
            high = mid - 1
        else:
            if mid == len(nums) - 1 or nums[mid + 1] > target:
                return mid
            else:
                low = mid + 1

    return -1


print(binary_search([3, 4, 4, 4, 5, 7, 8, 8, 9], 6))

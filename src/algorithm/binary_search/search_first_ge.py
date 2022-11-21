#
# 查找第一个大于等于 target 的 index
def binary_search(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if nums[mid] < target:
            low = mid + 1
        else:
            if mid == 0 or nums[mid - 1] < target:
                return mid
            else:
                high = mid - 1

    return -1


print(binary_search([3, 4, 4, 4, 5, 7, 8, 8, 9], 6))

"""
二分查找针对的是一个有序的数据集合，查找思想有点类似分治思想。每次都通过跟区间的中间元素对比，将待查找的区间缩小为之前的一半，直到找到要查找的元素，或者区间被缩小为 0。


O(logn) 这种对数时间复杂度
"""
from typing import List


def binary_search(nums: List[int], target: int) -> int:
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    n = len(nums)
    l = 0
    r = n - 1
    #
    while l <= r:
        mid = (l + r) >> 1
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1


res = binary_search([1, 2, 3], 3)
print(res)

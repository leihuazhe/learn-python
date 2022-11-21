# 非常规的二分查找问题。如果有序数组是一个循环有序数组，比如 4，5，6，1，2，3。针对这种情况，如何实现一个求“值等于给定值”的二分查找算法呢？
# lc.33 https://leetcode.cn/problems/search-in-rotated-sorted-array/


from typing import List


class Solution:
    """
    There is an integer array nums sorted in ascending order (with distinct values).
    旋转后的有序数组
    """

    def search(self, nums: List[int], target: int) -> int:
        n = len(nums) - 1
        low = 0
        high = n
        while low <= high:
            mid = low + ((high - low) >> 1)
            if nums[mid] == target:
                return mid

            if nums[0] <= nums[mid]:
                if nums[0] <= target and target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target and target <= nums[n]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

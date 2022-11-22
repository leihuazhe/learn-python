class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        l_sum, r_sum = 0, sum(nums)

        for i, v in enumerate(nums):
            r_sum -= v
            if l_sum == r_sum:
                return i
            l_sum += v
        return -1

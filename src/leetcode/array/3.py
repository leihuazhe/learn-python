class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = set()
        # 滑动窗口 [l...r]
        # 因为窗口是前闭后闭的,初始化的时候不能由一个存在的[0,0]的滑动窗口,所以要把 r 设置成 -1
        l = 0
        r = -1
        res = 0
        # 思路是限制l的范围,对 r 和 l 进行滑动.
        # 要注意数组越界的问题,r 如果到了右边界后,他就不能再动了，只能去处理 l 了。
        while l < len(s):
            if r + 1 < len(s) and s[r + 1] not in freq:
                freq.add(s[r + 1])
                r += 1
            else:
                freq.remove(s[l])
                l += 1
            res = max(res, r - l + 1)

        return res


s = Solution()

print(s.lengthOfLongestSubstring("abcajhgdeaaa"))

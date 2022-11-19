from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def do_merge(items, cursor, first, res):
            if cursor == len(items) - 1:
                return res

            second = items[cursor + 1]
            if first[1] >= second[0]:
                res.pop(-1)
                res.append([min(first[0], second[0]), max(first[1], second[1])])
            else:
                if cursor == 0:
                    res.pop(-1)
                    res.append(first)
                res.append(second)

            return do_merge(items, cursor + 1, res[-1], res)

        if len(intervals) == 1:
            return intervals
        intervals.sort(key=lambda x: (x[0], x[1]))
        return do_merge(intervals, 0, intervals[0], [[0]])


res = Solution().merge([[1, 4], [5, 6]])
print(res)

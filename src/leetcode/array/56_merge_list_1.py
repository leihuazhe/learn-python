from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def do_merge(items, cursor, first, new_intervals):
            if cursor == len(items) - 1:
                return new_intervals

            second = items[cursor + 1]
            if first[1] >= second[0]:
                if new_intervals:
                    new_intervals.pop(-1)
                new_intervals.append([min(first[0], second[0]), max(first[1], second[1])])
            else:
                if cursor == 0:
                    new_intervals.append(first)
                new_intervals.append(second)

            return do_merge(items, cursor + 1, new_intervals[-1], new_intervals)

        if len(intervals) == 1:
            return intervals
        intervals.sort(key=lambda x: (x[0], x[1]))
        return do_merge(intervals, 0, intervals[0], list())


res = Solution().merge([[1, 4], [0, 2], [3, 5]])
print(res)

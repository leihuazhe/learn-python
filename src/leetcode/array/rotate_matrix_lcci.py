# https://leetcode.cn/problems/rotate-matrix-lcci/
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = zip(*matrix[::-1])


matrix = [[1, 3], [2, 4], [3, 6]]
# 从右侧开始,以步长1向左截取
print(matrix[:])
print(matrix[::-1])
print(list(zip(*matrix[::-1])))

"""

1 3   3 6
2 4   2 4
3 6   1 3

"""

l1 = [1, 3, 5, 7, 9, 11]
l2 = [2, 4, 6, 8, 10]

# 第3个参数是步长
print(l1[:3:2])
print(l1[3:6:2])

# zip
zipped = zip(l1, l2)
print(list(zipped))

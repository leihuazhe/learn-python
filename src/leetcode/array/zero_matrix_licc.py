# https://leetcode.cn/problems/zero-matrix-lcci/
from typing import List


# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         if matrix is None:
#             return
#         # 要取内侧的最大 len
#         o_n = len(matrix)
#         i_n = len(matrix[0])
#
#         tempMatrix = []
#
#         for i, arr in enumerate(matrix):
#             for j, value in enumerate(arr):
#                 if value == 0:
#                     tempMatrix.append([i, j])
#
#         for m in tempMatrix:
#             i = m[0]
#             j = m[1]
#
#             for t in range(0, i_n):
#                 matrix[i][t] = 0
#
#             for t in range(0, o_n):
#                 matrix[t][j] = 0


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if matrix is None:
            return

        m = len(matrix)
        n = len(matrix[0])

        row = [False] * m
        col = [False] * n

        for i in range(0, m):
            for j in range(0, n):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True

        for i in range(0, m):
            for j in range(0, n):
                if row[i] or col[j]:
                    matrix[i][j] = 0


s = Solution()

# z1
z1 = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]
s.setZeroes(z1)
print(z1)

z2 = [
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
]
s.setZeroes(z2)
print(z2)

z3 = [
    [0, 1]

]
s.setZeroes(z3)
print(z3)

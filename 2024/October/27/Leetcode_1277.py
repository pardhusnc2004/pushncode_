'''
    Leetcode Daily Question (27-10-2024)
    1277. Count Square Submatrices with All Ones
    Python3 solution
'''
from typing import List, Optional

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        res = 0
        for i in range(m-2, -1, -1):
            for j in range(n-1, -1, -1):
                if j+1 < n:
                    if matrix[i][j]:
                        res += 1+min(matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1])
                        matrix[i][j] = min(matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1])+1
                else:
                    if matrix[i][j]:
                        res += 1
        res += sum(matrix[-1])
        return res
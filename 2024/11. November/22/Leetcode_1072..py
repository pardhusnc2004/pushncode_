'''
    Leetcode Daily Question (22-11-2024)
    1072. Flip Columns For Maximum Number of Equal Rows
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        if m < 2:
            return m
        
        def getRowHash(i: int) -> str:
            nonlocal matrix, n
            flip = matrix[i][0] == 1

            row_hash = []
            for j in range(n):
                row_hash.append(str(matrix[i][j] if not flip else (1 - matrix[i][j])))
            return ''.join(row_hash)
        return max(Counter(getRowHash(i) for i in range(m)).values())
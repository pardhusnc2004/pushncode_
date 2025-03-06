'''
    Leetcode Daily Question (06-03-2025)
    2965. Find Missing and Repeated Values
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        _total, _sqTotal, _required, _sqRequired = 0, 0, (n**2*(n**2+1))//2, (n**2*(n**2+1)*(2*n**2+1))//6
        for i in range(n):
            for j in range(n):
                tmp = grid[i][j]
                _total += tmp
                _sqTotal += tmp**2
        
        '''
            n = 2, 1 repeated and 2 is missing, 
            1+1+3+4
            1+2+3+4
        '''

        _diff = _required - _total
        _sqDiff = _sqRequired - _sqTotal

        _sum = _sqDiff // _diff

        x = (_sum + _diff) // 2
        y = _sum - x

        return [y, x]
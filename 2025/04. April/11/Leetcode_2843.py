'''
    Leetcode Daily Question (11-04-2025)
    2843. Count Symmetric Integers
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        
        res = 0

        for x in range(low, high+1):
            tmp = str(x)
            n = len(tmp)
            if n%2 == 1:
                continue
            left_sum, right_sum = 0, 0
            for i in range(n//2):
                left_sum += int(tmp[i])
                right_sum += int(tmp[-i-1])
            if left_sum == right_sum:
                res += 1
        
        return res
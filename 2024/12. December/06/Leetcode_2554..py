'''
    Leetcode Daily Question (06-12-2024)
    2554. Maximum Number of Integers to Choose From a Range I
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        canTake = []
        banned = set(banned)
        for i in range(1, n+1):
            if i not in banned:
                canTake.append(i)
        res = 0

        curSum = 0
        for i in canTake:
            if curSum+i <= maxSum:
                res += 1
                curSum += i
            else:
                break

        return res
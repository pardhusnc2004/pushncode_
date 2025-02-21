'''
    Leetcode Daily Question (20-02-2025)
    1980. Find Unique Binary String
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        if n is 1:
            return "1" if "1" not in nums else "0"
        nums = [int(i, 2) for i in nums]
        s = set(nums)
        def formatToBinary(i):
            b = bin(i)[2:]
            return "0"*(n-len(b))+b
        for i in range(n):
            if i not in s:
                return formatToBinary(i)
        return formatToBinary(n+1)
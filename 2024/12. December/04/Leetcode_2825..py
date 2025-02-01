'''
    Leetcode Daily Question (04-12-2024)
    2825. Make String a Subsequence Using Cyclic Increments
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        m, n = len(str1), len(str2)
        def getNextChar(a):
            idx = ord(a)-ord('a')+1
            idx %= 26
            return chr(ord('a')+idx)
        j = 0
        for i in range(m):
            if str2[j] in [str1[i], getNextChar(str1[i])]:
                j += 1
            if j == n:
                return True
        return j >= n
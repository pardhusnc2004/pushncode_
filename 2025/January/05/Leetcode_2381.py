'''
    Leetcode Daily Question (05-01-2025)
    2381. Shifting Letters II
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        final = [0]*(n+1)
        for l, r, _ in shifts:
            if _ == 1:
                final[l] += 1
                final[r+1] -= 1
            else:
                final[l] -= 1
                final[r+1] += 1
        for i in range(n):
            final[i+1] += final[i]
        # print(final)
        res = ""
        for i in range(n):
            tmp = s[i]
            offset = final[i]%26
            res += chr(((ord(tmp)-ord('a'))+offset)%26+ord('a'))
        return res
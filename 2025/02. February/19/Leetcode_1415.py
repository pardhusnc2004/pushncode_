'''
    Leetcode Daily Question (19-02-2025)
    1415. The k-th Lexicographical String of All Happy Strings of Length n
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        def go(i, ds):
            if i == n:
                res.append(ds[:])
                if len(res) == k:
                    return True
                return False
            if not ds:
                for ch in range(3):
                    if go(i+1, chr(ord('a')+ch)):
                        return True
            else:
                for ch in range(3):
                    char = chr(ord('a')+ch)
                    if ds[-1] != char:
                        if go(i+1, ds+char):
                            return True
            return False
        if go(0, ""):
            return res[-1]
        return ""
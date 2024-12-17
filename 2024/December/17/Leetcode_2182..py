'''
    Leetcode Daily Question (17-12-2024)
    2182. Construct String With Repeat Limit
    Python3 solution
'''
from typing import *
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        c = Counter(s)
        res = ""
        keys = sorted(list(c.keys()))
        keys.reverse()
        i, j = 0, 1
        # print(keys)
        while i < len(keys):
            # print(i, j, c)
            if c[keys[i]] <= repeatLimit:
                res += keys[i]*c[keys[i]]
                del c[keys[i]]
                i = j
                j += 1
            else:
                res += keys[i]*repeatLimit
                c[keys[i]] -= repeatLimit
                if j >= len(keys):
                    break
                if c[keys[j]] == 0:
                    del c[keys[j]]
                    j += 1
                if j >= len(keys):
                    break
                res += keys[j]
                c[keys[j]] -= 1
            # print(res)
        return res
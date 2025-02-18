'''
    Leetcode Daily Question (18-02-2025)
    2375. Construct Smallest Number From DI String
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res = []
        def go(i, st):
            if i == len(pattern):
                res.append(st)
                # print(st)
                return True
            for k in range(1, 10):
                if str(k) not in st:
                    if pattern[i] == 'I':
                        if k > int(st[-1]):
                            if go(i+1, st+str(k)):
                                return True
                    else:
                        if k < int(st[-1]):
                            if go(i+1, st+str(k)):
                                return True
            return False
        for k in range(1, 10):
            if go(0, str(k)):
                return res[0]
        return res[0]
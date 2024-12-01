'''
    Leetcode Daily Question (01-12-2024)
    1346. Check If N and Its Double Exist
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d = {}
        for i in arr:
            if i*2 in d:
                return True
            if i&1 == 0:
                if i//2 in d:
                    return True
            d[i] = 1
        return False
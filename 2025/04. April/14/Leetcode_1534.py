'''
    Leetcode Daily Question (14-04-2025)
    1534. Count Good Triplets
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    tmp1, tmp2, tmp3 = abs(arr[i]-arr[j]), abs(arr[j]-arr[k]), abs(arr[k]-arr[i])
                    if tmp1 <= a and tmp2 <= b and tmp3 <= c:
                        res += 1
        return res
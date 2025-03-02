'''
    Leetcode Daily Question (02-03-2025)
    2570. Merge Two 2D Arrays by Summing Values
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d = {}
        for i, j in nums1:
            d[i] = d.get(i, 0)+j
        for i, j in nums2:
            d[i] = d.get(i, 0)+j        
        return list(sorted(d.items()))
'''
    Leetcode Daily Question (06-01-2025)
    1769. Minimum Number of Operations to Move All Balls to Each Box
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = [0]*n
        boxes = list(map(int, boxes))
        
        for i in range(n):
            for j in range(n):
                res[j] += boxes[i]*abs(i-j)

        return res
'''
    Leetcode Daily Question (05-03-2025)
    2579. Count Total Number of Colored Cells
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def coloredCells(self, n: int) -> int:
        return 1+(n*(n-1)*2)
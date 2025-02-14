'''
    Leetcode Daily Question (14-02-2025)
    1352. Product of the Last K Numbers
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class ProductOfNumbers:

    def __init__(self):
        self.arr = [[1, 1]]
        self.Zero = -1

    def add(self, num: int) -> None:
        if not num:
            self.arr.append([1, 0])
            self.Zero = len(self.arr)-1
        else:
            if self.arr:
                self.arr.append([self.arr[-1][0]*num, 1])
            else:
                self.arr.append([num, 1])

    def getProduct(self, k: int) -> int:
        if self.Zero > -1:
            if k >= len(self.arr)-self.Zero:
                return 0
        return self.arr[-1][0]//self.arr[-k-1][0]
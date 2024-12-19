'''
    Leetcode Daily Question (18-12-2024)
    1475. Final Prices With a Special Discount in a Shop
    Python3 solution
'''
from typing import *
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        n = len(prices)
        res = [-1]*n
        for i in range(n-1, -1, -1):
            while stack and prices[i] < prices[stack[-1]]:
                stack.pop()
            if stack:
                res[i] = prices[i]-prices[stack[-1]]
            else:
                res[i] = prices[i]
            stack.append(i)
        return res
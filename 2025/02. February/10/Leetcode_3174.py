'''
    Leetcode Daily Question (10-02-2025)
    3174. Clear Digits
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for i in s:
            if i.isalpha():
                stack.append(i)
            else:
                if stack:
                    stack.pop()
        return "".join(stack)
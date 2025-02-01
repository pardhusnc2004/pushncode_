'''
    Leetcode Daily Question (18-11-2024)
    1652. Defuse the Bomb
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        res = [0]*len(code)
        if not k:
            return res
        left, right, curSum = 1, k, 0
        if k < 0:
            left = len(code) - abs(k)
            right = len(code) - 1
        for i in range(left, right + 1):
            curSum += code[i]
        for i in range(len(code)):
            res[i] = curSum
            curSum -= code[left % len(code)]
            curSum += code[(right + 1) % len(code)]
            left += 1
            right += 1
        return res
'''
    Leetcode Daily Question (17-01-2025)
    2683. Neighboring Bitwise XOR
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        if n == 1:
            return derived[0] == 0
        if n == 2:
            return sum(derived) in [n, 0]
        
        binary = [1]
        for i in range(n):
            if derived[i] == 0:
                binary.append(binary[-1])
            else:
                binary.append(binary[-1]^1)
        
        return binary[0] == binary[-1]
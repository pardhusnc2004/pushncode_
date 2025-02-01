'''
    Leetcode Daily Question (08-01-2025)
    3042. Count Prefix and Suffix Pairs I
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(a, b):
            if len(b) < len(a):
                return False
            return b[:len(a)] == a and b[::-1][:len(a)][::-1] == a
        res = 0
        n = len(words)
        for i in range(n):
            for j in range(i+1, n):
                if isPrefixAndSuffix(words[i], words[j]):
                    res += 1
        return res
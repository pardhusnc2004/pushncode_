'''
    Leetcode Daily Question (10-01-2025)
    916. Word Subsets
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        d = defaultdict(int)
        for word in words2:
            c = Counter(word)
            for letter in c:
                d[letter] = max(d[letter], c[letter])
        # print(d)
        def isSubset(word):
            c = Counter(word)
            for letter in d:
                if c.get(letter, 0) < d[letter]:
                    return False
            return True
        res = []
        for word in words1:
            if isSubset(word):
                res.append(word)
        return res
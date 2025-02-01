'''
    Leetcode Daily Question (07-01-2025)
    1408. String Matching in an Array
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words = set(words)
        res = set()
        for word in words:
            for subs in words:
                if word != subs and subs in word:
                    res.add(subs)
        return list(res)
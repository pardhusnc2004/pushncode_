'''
    Leetcode Daily Question (02-01-2025)
    2559. Count Vowel Strings in Ranges
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        nums = [0]
        for word in words:
            if word[0] in 'aeiou' and word[-1] in 'aeiou':
                nums.append(1+nums[-1])
            else:
                nums.append(nums[-1])
        
        res = []
        for l, r in queries:
            res.append(nums[r+1]-nums[l])
        return res
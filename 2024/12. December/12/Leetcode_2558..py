'''
    Leetcode Daily Question (12-12-2024)
    2779. Maximum Beauty of an Array After Applying Operation
    Python3 solution
'''
from typing import *
from collections import *
from bisect import *
from math import *
from heapq import *


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        arr = []
        for num in nums:
            arr.append((num-k, "l"))
        for num in nums:
            arr.append((num+k, "r"))
        arr.sort()
        res = 0
        cur = 0
        for _, i in arr:
            if i == 'l':
                cur += 1
            else:
                res = max(res, cur)
                cur -= 1
        return max(res, cur)

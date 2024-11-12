'''
    Leetcode Daily Question (12-11-2024)
    2070. Most Beautiful Item for Each Query
    Python3 solution
'''
from typing import List
from collections import *

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        res = []
        dp = defaultdict(int)
        for i, j in items:
            dp[i] = max(dp[i], j)
        items = list([i, j] for i, j in sorted(dp.items()))
        for i in range(1, len(items)):
            items[i][1] = max(items[i][1], items[i-1][1])
        for query in queries:
            l, r = 0, len(items)-1
            curRes = 0
            while l <= r:
                m = (l+r) >> 1
                if items[m][0] <= query:
                    curRes = items[m][1]
                    l = m+1
                else:
                    r = m-1
            res.append(curRes)

        return res
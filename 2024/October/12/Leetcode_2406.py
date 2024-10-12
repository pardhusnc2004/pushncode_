'''
    Leetcode Daily Question (12-10-2024)
    2406. Divide Intervals Into Minimum Number of Groups
    Python3 solution
'''

from typing import List

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        test = []
        for start, end in intervals:
            test.append([start, 1])
            test.append([end, -1])
        test.sort(key = lambda x:[x[0], -x[1]])
        cur, res = 0, 0
        for _, add in test:
            cur += add
            res = max(res, cur)
        return res
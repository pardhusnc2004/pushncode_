'''
    GeeksforGeeks Daily Question (22-10-2024)
    Sub-arrays with equal number of occurences
    Python3 solution
'''

from collections import defaultdict
class Solution:
    def sameOccurrence(self, arr, x, y):
        # code here
        d = defaultdict(int)
        d[0] = 1
        res = 0
        xCnt, yCnt = 0, 0
        for i in arr:
            if i == x:
                xCnt += 1
            if i == y:
                yCnt += 1
            diff = xCnt - yCnt
            res += d[diff]
            d[diff] += 1
        return res
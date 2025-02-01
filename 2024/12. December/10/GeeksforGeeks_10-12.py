'''
    GeeksforGeeks Daily Question (10-12-2024)
    Non-overlapping Intervals
    Python3 solution
'''

class Solution:
    def minRemoval(self, intervals):
        # Code here
        intervals.sort(key = lambda x:x[1])
        # print(intervals)
        res = 0
        last = 0
        for i, j in intervals:
            if i >= last:
                last = j
                continue
            res += 1
        return res
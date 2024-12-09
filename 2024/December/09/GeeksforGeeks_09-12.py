'''
    GeeksforGeeks Daily Question (09-12-2024)
    Insert Interval
    Python3 solution
'''

class Solution:
    def insertInterval(self, intervals, newInterval):
        # Code here
        intervals.append(newInterval)
        intervals.sort()
        res = []
        for st, end in intervals:
            if not res or st > res[-1][-1]:
                res.append([st, end])
            else:
                res[-1][-1] = max(res[-1][-1], end)
        return res
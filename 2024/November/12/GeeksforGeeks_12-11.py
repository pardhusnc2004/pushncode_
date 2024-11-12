'''
    GeeksforGeeks Daily Question (12-11-2024)
    Meeting Rooms
    Python3 solution
'''

class Solution:
    def canAttend(self,arr):
        # Your Code Here
        meetings = []
        for start, end in arr:
            meetings.append((start, 1))
            meetings.append((end, -1))
        meetings.sort()
        res = 0
        cur = 0
        for i, _ in meetings:
            cur += _
            res = max(res, cur)
        
        return res == 1

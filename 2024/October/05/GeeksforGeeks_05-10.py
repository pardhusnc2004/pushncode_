'''
    GeeksforGeeks Daily Question (05-10-2024)
    Not a subset sum
    Python3 solution
'''

class Solution:
    def findSmallest(self, arr):
        # code here
        maxReach = 0
        cur = 1
        for i in arr:
            if i > cur:
                return cur
            maxReach += i
            cur = maxReach+1
        return cur
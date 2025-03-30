'''
    GeeksforGeeks Daily Question (30-03-2025)
    Gas Station
    Python3 solution
'''

class Solution:
    def startStation(self, gas, cost):
        # Your code here
        n = len(gas)
        cur, prev = 0, 0
        res = 0
        for i in range(n):
            cur += gas[i] - cost[i]
            if cur < 0:
                res = i+1
                prev += cur
                cur = 0
        return res if cur+prev >= 0 else -1
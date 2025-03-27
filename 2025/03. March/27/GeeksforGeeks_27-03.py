'''
    GeeksforGeeks Daily Question (27-03-2025)
    Minimum Platforms
    Python3 solution
'''

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        # code here
        n = len(arr)
        res = 0
        cur = 0
        
        events = []
        for i, j in zip(arr, dep):
            events.append((i, -1))
            events.append((j, 1))
        events.sort()
        
        for _, d in events:
            cur -= d
            res = max(res, cur)
        
        return res
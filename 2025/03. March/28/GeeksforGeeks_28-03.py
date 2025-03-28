'''
    GeeksforGeeks Daily Question (28-03-2025)
    Activity Selection
    Python3 solution
'''

class Solution:
    def activitySelection(self, start, finish):
        #code here
        events = [(start[i], finish[i]) for i in range(len(start))]
        events.sort(key = lambda x: x[1])
        
        res = 1
        prv = events[0][1]
        
        for st, fi in events[1:]:
            if st > prv:
                res += 1
                prv = max(prv, fi)
        
        return res

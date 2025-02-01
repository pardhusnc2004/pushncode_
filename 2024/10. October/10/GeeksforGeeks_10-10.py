'''
    GeeksforGeeks Daily Question (10-10-2024)
    Max distance between same elements
    Python3 solution
'''

class Solution:
    def maxDistance(self, arr):
        # Code here
        d = {}
        for idx, i in enumerate(arr):
            if i not in d:
                d[i] = [idx, idx]
            else:
                d[i][1] = idx
        return max(d[i][1]-d[i][0] for i in d)
'''
    GeeksforGeeks Daily Question (03-03-2025)
    Longest Bounded-Difference Subarray
    Python3 solution
'''

class Solution:
    def longestSubarray(self, arr, x):
        start, end = -1, -1
        l = 0
        d = {}
        for r in range(len(arr)):
            d[arr[r]] = d.get(arr[r], 0)+1
            while abs(min(d) - max(d)) > x:
                d[arr[l]] -= 1
                if not d[arr[l]]:
                    del d[arr[l]]
                l += 1
            if start == -1 or end == -1 or (end-start) < (r-l):
                start = l
                end = r
        return arr[start:end+1]
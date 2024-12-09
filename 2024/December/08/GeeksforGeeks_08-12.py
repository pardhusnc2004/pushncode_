'''
    GeeksforGeeks Daily Question (08-12-2024)
    Overlapping Intervals
    Python3 solution
'''

class Solution:
    def mergeOverlap(self, arr):
        arr.sort(key=lambda x: x[0])
        merged = []
        for interval in arr:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

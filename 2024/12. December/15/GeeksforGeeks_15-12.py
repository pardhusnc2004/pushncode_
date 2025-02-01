'''
    GeeksforGeeks Daily Question (15-12-2024)
    Peak element
    Python3 solution
'''

class Solution:   
    def peakElement(self,arr):
        # Code here
        n = len(arr)
        if n == 1:
            return 0
        if arr[0] > arr[1]:
            return 0
        if arr[-1] > arr[-2]:
            return n-1
        for i in range(1, n-1):
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                return i
        return -1

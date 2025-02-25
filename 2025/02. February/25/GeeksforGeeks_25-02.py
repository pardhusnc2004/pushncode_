'''
    GeeksforGeeks Daily Question (25-02-2025)
    Histogram Max Rectangular Area
    Python3 solution
'''

class Solution:
    def getMaxArea(self,arr):
        #code here
        res = 0
        stack = []
        n = len(arr)        
        for i in range(n+1):
            while stack and (i == n or arr[i] <= arr[stack[-1]]):
                height = arr[stack.pop()]
                width = i
                if stack:
                    width = i-stack[-1]-1
                res = max(res, height*width)
            stack.append(i)
        return res

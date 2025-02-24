'''
    GeeksforGeeks Daily Question (24-02-2025)
    Stock span problem
    Python3 solution
'''

class Solution:
    def calculateSpan(self, arr):
        #write code here
        n = len(arr)
        stack = []
        
        res = [1]*n
        for i in range(n):
            while stack and arr[i] >= arr[stack[-1]]:
                stack.pop()
            if stack:
                res[i] = i-stack[-1]
            else:
                res[i] = i+1
            stack.append(i)
                
        return res
        
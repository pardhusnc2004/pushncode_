'''
    GeeksforGeeks Daily Question (23-02-2025)
    Next Greater Element
    Python3 solution
'''

class Solution:
    # Function to find the next greater element for each element of the array.
    def nextLargerElement(self, arr):
        # code here
        stack = []
        n = len(arr)
        res = [-1]*n
        for i in range(n-1, -1, -1):
            while stack and arr[i] >= arr[stack[-1]]:
                stack.pop()
            if stack:
                res[i] = arr[stack[-1]]
            stack.append(i)
        return res

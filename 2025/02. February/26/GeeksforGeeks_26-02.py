'''
    GeeksforGeeks Daily Question (26-02-2025)
    Maximum of minimum for every window size
    Python3 solution
'''

class Solution:
    def maxOfMins(self, arr):
       # code here
       n = len(arr)
       nxs = self.next_smaller(arr)
       pvs = self.previous_smaller(arr)
       result = [float('-inf')]*n
    
       for i in range(n):
           idx = nxs[i] - pvs[i] - 2
           result[idx] = max(result[idx], arr[i])
           
       stack = []
       
       for i in reversed(range(n)):
           
           while stack and result[stack[-1]] < result[i]:
               stack.pop()
           
           if stack: result[i] = max(result[i], result[stack[-1]])
           stack.append(i)
           
       return result
       
    def next_smaller(self, arr):
        n = len(arr)
        nxs = [n]*n
        stack = []
        
        for i in reversed(range(n)):
            
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            
            if stack: nxs[i] = stack[-1]
            stack.append(i)
        
        return nxs
    
    def previous_smaller(self, arr):
        n = len(arr)
        pxs = [-1]*n
        stack = []
        
        for i in range(n):
            
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            
            if stack: pxs[i] = stack[-1]
            stack.append(i)
        
        return pxs
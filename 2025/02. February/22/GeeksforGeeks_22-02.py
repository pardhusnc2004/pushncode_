'''
    GeeksforGeeks Daily Question (22-02-2025)
    Longest valid Parentheses
    Python3 solution
'''

class Solution:
    def maxLength(self, s):
        # code here
        stack = [-1]
        res = 0
        n = len(s)
        for i in range(n):
            if s[i] == ')':
                stack.pop()
                if not stack:
                    stack.append(i)
                res = max(res, i-stack[-1])
                    
            else:
                stack.append(i)
        return res
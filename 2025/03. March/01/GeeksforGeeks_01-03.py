'''
    GeeksforGeeks Daily Question (01-03-2025)
    Decode the string
    Python3 solution
'''

class Solution:
    def decodedString(self, s):
        # code here
        stack = []
        
        cur = 0
        for i in s:
            if i.isdigit():
                cur = cur*10+int(i)
            else:
                if i == '[':
                    stack.append(cur)
                    stack.append(']')
                    cur = 0
                elif i == ']':
                    tmp = ""
                    while stack and stack[-1] != i:
                        tmp += stack.pop()
                    stack.pop()
                    stack.append(tmp*stack.pop())
                    
                else:
                    stack.append(i)
        res = ""
        stack.reverse()
        while stack:
            res += stack.pop()[::-1]
        return res

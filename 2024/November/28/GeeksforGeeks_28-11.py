'''
    GeeksforGeeks Daily Question (28-11-2024)
    Implement Atoi
    Python3 solution
'''

from math import inf
#Complete this function
#User function template for Python
class Solution:
    def myAtoi(self, s):
        # Code here
        s = list(s)
        while s and s[0].isspace():
            s.pop(0)
        if not s:
            return 0
        i = 0
        sign = 1
        if s[0] in ['+', '-']:
            if s[0] == '-':
                sign *= -1
            i += 1
        cur = 0

        while i < len(s):
            if s[i].isdigit():
                cur = cur*10+int(s[i])
            else:
                break
            i += 1
        # print(i)
        return max(-2147483648, min(cur*sign, 2147483647))


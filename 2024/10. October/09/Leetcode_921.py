'''
    Leetcode Daily Question (09-10-2024)
    921. Minimum Add to Make Parentheses Valid
    Python3 solution
'''

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = 0
        extra = 0
        for i in s:
            if i == '(':
                res+=1
            else:
                if res:
                    res-=1
                else:
                    extra+=1
        return res+extra
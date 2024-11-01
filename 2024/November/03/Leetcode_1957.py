'''
    Leetcode Daily Question (01-11-2024)
    1957. Delete Characters to Make Fancy String
    Python3 solution
'''

class Solution:
    def makeFancyString(self, s: str) -> str:
        res = ""
        prv = '-'
        cnt = 0
        for i in s:
            if i == prv:
                cnt += 1
            else:
                res += prv*(min(2, cnt))
                prv = i
                cnt = 1
        res += prv*min(2, cnt)
        return res
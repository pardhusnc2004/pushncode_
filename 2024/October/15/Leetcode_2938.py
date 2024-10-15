'''
    Leetcode Daily Question (15-10-2024)
    2938. Separate Black and White Balls
    Python3 solution
'''

class Solution:
    def minimumSteps(self, s: str) -> int:
        black = 0
        res = 0
        for i in s:
            if i == '1':
                black += 1
            else:
                res += black
        return res
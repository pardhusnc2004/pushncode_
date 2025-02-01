'''
    Leetcode Daily Question (03-11-2024)
    796. Rotate String
    Python3 solution
'''

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        return goal in s+s

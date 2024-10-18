'''
    GeeksforGeeks Daily Question (18-10-2024)
    Single Number
    Python3 solution
'''

class Solution:
    
    def getSingle(self,arr):
        # code here
        res = 0
        for i in arr:
            res ^= i
        return res
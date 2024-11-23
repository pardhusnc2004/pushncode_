'''
    GeeksforGeeks Daily Question (22-11-2024)
    Stock Buy and Sell – Max one Transaction Allowed
    Python3 solution
'''

class Solution:
    def maximumProfit(self, prices):
        # code here
        res = 0
        curmin = 1e9
        for i in prices:
            if curmin > i:
                curmin = i
            else:
                res = max(res, i-curmin)
        return res
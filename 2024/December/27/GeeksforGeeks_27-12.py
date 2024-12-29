'''
    GeeksforGeeks Daily Question (27-12-2024)
    Count pairs with given sum
    Python3 solution
'''

class Solution:
    #Complete the below function
    def countPairs(self,arr, target):
        #Your code here
        d = {}
        res = 0
        for i in arr:
            if target-i in d:
                res += d[target-i]
            d[i] = d.get(i, 0)+1
        return res
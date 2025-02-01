'''
    GeeksforGeeks Daily Question (07-01-2025)
    Pair with given sum in a sorted array
    Python3 solution
'''

class Solution:
    def countPairs (self, arr, target) : 
        #Complete the function
        d = {}
        res = 0
        for i in arr:
            if target-i in d:
                res += d[target-i]
            d[i] = d.get(i, 0)+1
        return res
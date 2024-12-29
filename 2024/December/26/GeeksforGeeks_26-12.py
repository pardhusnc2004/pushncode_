'''
    GeeksforGeeks Daily Question (26-12-2024)
    Two Sum - Pair with Given Sum
    Python3 solution
'''

class Solution:
    def twoSum(self,arr, x):
        # code here
        n = len(arr)
        d = {}
        for i in arr:
            rem = x-i
            if rem in d:
                return True
            d[i] = 1
        return False
            


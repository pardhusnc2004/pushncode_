'''
    GeeksforGeeks Daily Question (14-01-2025)
    Equilibrium Point
    Python3 solution
'''

class Solution:
    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        # code here
        SUM = sum(arr)
        cur = 0
        n = len(arr)
        
        for i in range(n):
            SUM -= arr[i]
            if SUM == cur:
                return i
            cur += arr[i]

        return -1
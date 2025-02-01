'''
    GeeksforGeeks Daily Question (07-11-2024)
    Split array in three equal sum subarrays
    Python3 solution
'''

class Solution:
    
    def findSplit(self, arr):
        # Return an array of possible answer, driver code will judge and return true or false based on
        n = len(arr)
        d = {}
        cur = 0
        revPref = [0]*(n)
        revPref[-1] = arr[-1]
        for i in range(n-2, -1, -1):
            revPref[i] = revPref[i+1]+arr[i]
        revPref += [0]
        # print(revPref)
        for i in range(n):
            cur += arr[i]
            if cur&1 == 0 and cur//2 in d:
                if cur//2 == revPref[i+1]:
                    return [d[cur//2], i]
            d[cur] = i
        return [-1, -1]
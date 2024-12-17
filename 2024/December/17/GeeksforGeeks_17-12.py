'''
    GeeksforGeeks Daily Question (17-12-2024)
    Aggressive Cows
    Python3 solution
'''

class Solution:
    def aggressiveCows(self,arr, k):
        res = 0
        n = len(arr)
        arr.sort()
        i, j = 1, max(arr)
        while i <= j:
            mid = (i+j)//2
            if self.helper(arr, n, k, mid):
                res = mid
                i = mid+1
            else:
                j = mid-1
        return res
    def helper(self, arr, n, k, mid):
        res = 1
        cur = arr[0]
        for i in range(1, n):
            if arr[i] - cur >= mid:
                res += 1
                cur = arr[i]
            
        return res >= k

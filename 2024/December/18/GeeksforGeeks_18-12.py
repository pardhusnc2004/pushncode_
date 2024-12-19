'''
    GeeksforGeeks Daily Question (17-12-2024)
    Allocate Minimum Pages
    Python3 solution
'''

class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self, arr, k):
        #code here
        def good(mid):
            flag = 1
            cur = 0
            for i in arr:
                if cur+i <= mid:
                    cur += i
                else:
                    flag += 1
                    cur = i
            return flag <= k
            pass
        if k > len(arr):
            return -1
        l, r = max(arr), sum(arr)
        res = -1
        while l <= r:
            mid = (l+r) >> 1
            if good(mid):
                res = mid
                r = mid-1
            else:
                l = mid+1
        return res

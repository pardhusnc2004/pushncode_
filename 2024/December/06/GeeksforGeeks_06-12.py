'''
    GeeksforGeeks Daily Question (06-12-2024)
    Find H-Index
    Python3 solution
'''

class Solution:
    # Function to find hIndex
    def hIndex(self, citations):
        #code here
        n = len(citations)
        def good(mid):
            cur = 0
            for i in citations:
                if i >= mid:
                    cur += 1
                    if cur == mid:
                        return True
                        
            return False
        res = 0
        l, r = 0, n
        while l <= r:
            mid = (l+r) >> 1
            if good(mid):
               res = mid
               l = mid+1
            else:
                r = mid-1
        return res
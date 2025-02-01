'''
    GeeksforGeeks Daily Question (31-12-2024)
    Longest Consecutive Subsequence
    Python3 solution
'''

class Solution:
    
    # arr[] : the input array
    #Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self,arr):
        #code here
        res = 0
        arr = set(arr)
        for i in arr:
            if i-1 in arr:
                continue
            else:
                cur = 1
                kk = i+1
                while kk in arr:
                    kk += 1
                    cur += 1
                res = max(res, cur)
        return res
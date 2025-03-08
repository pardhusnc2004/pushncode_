'''
    GeeksforGeeks Daily Question (08-03-2025)
    Longest Palindrome in a String
    Python3 solution
'''

class Solution:
    def longestPalindrome(self, S):
        # code here
        res = S[0]
        n = len(S)
        for i in range(1, n):
            #even
            l, r = i-1, i
            cur = ""
            while l>=0 and r<n and S[l]==S[r]:
                cur = S[l]+cur+S[r]
                l-=1
                r+=1
            if len(res) < len(cur):
                res = cur
            #odd
            cur = S[i]
            l, r = i-1, i+1
            while l>=0 and r<n and S[l]==S[r]:
                cur = S[l]+cur+S[r]
                l-=1
                r+=1
            if len(res) < len(cur):
                res = cur
        return res


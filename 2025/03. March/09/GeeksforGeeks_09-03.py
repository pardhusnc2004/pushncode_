'''
    GeeksforGeeks Daily Question (09-03-2025)
    Palindrome SubStrings
    Python3 solution
'''

class Solution:

    def countPS(self, s):
        
        n=len(s)
        ans=0
        for i in range(n):
            for h in (i,i+1):
                l=i-1
                while l>=0 and h<n and s[l]==s[h]:
                    l-=1
                    h+=1
                    ans+=1
        return ans
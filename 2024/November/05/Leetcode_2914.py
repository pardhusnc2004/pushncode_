'''
    Leetcode Daily Question (05-11-2024)
    2914. Minimum Number of Changes to Make Binary String Beautiful
    Python3 solution
'''

class Solution:
    def minChanges(self, s: str) -> int:
        zero=0
        one=0
        count=0
        for i in range(len(s)):
            if(s[i]=="0"):
                zero+=1
                if(one%2!=0):
                    count+=1
                    zero=0
                    one+=1
                else:
                    one=0
            else:
                one+=1
                if(zero%2!=0):
                    count+=1
                    one=0
                    zero+=1
                else:
                    zero=0
        return count
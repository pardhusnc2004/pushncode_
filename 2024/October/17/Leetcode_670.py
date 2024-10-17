'''
    Leetcode Daily Question (17-10-2024)
    670. Maximum Swap
    Python3 solution
'''

class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        ls = [int(i) for i in s]
        if ls[::-1] == sorted(ls):
            return num
        sortedls = sorted(ls)
        j = 0
        i = len(s)-1
        while i >= 0 and j < len(s) and int(s[j]) == int(sortedls[i]):
            j += 1
            i -= 1
        req = int(sortedls[i])
        ni = 0
        for k in range(len(s)-1, -1, -1):
            if int(s[k]) == req:
                ni = k
                break
        s[j], s[ni] = s[ni], s[j]
        return int("".join(s))
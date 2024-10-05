'''
    Leetcode Daily Question (05-10-2024)
    567. Permutation in String
    Python3 solution
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        req = [0]*26
        def asc(n):
            return ord(n)-ord('a')
        for i in s1:
            req[asc(i)] += 1
        alpha = [0]*26
        def poss():
            for i in range(26):
                if alpha[i] != req[i]:
                    return False
            return True
        left = 0
        for right in range(len(s2)):
            idx = asc(s2[right])
            alpha[idx] += 1
            while alpha[idx] > req[idx]:
                alpha[asc(s2[left])] -= 1
                left += 1
            if poss():
                return True
        return False
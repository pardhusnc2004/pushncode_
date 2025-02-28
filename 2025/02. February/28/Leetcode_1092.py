'''
    Leetcode Daily Question (28-02-2025)
    1092. Shortest Common Supersequence 
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
        n1, n2 = len(s1), len(s2)
        lcs = [[0]*(n2+1) for _ in range(n1+1)]
        self.constructLCS(s1, s2, lcs)
        # for i in lcs:
        #     print(*i)
        
        return self.constructSCS(s1, s2, lcs)
    
    def constructSCS(self, s1, s2, lcs):
        n1, n2 = len(s1), len(s2)
        res = ""
        i, j = n1, n2
        while i > 0 and j > 0:
            if s1[i-1] == s2[j-1]:
                res += s1[i-1]
                i -= 1
                j -= 1
            else:
                if lcs[i-1][j] > lcs[i][j-1]:
                    res += s1[i-1]
                    i -= 1
                else:
                    res += s2[j-1]
                    j -= 1
        while i > 0:
            res += s1[i-1]
            i -= 1
        while j > 0:
            res += s2[j-1]
            j -= 1
        return res[::-1]
    
    def constructLCS(self, s1, s2, lcs):
        n1, n2 = len(s1), len(s2)
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if s1[i-1] == s2[j-1]:
                    lcs[i][j] = 1+lcs[i-1][j-1]
                else:
                    lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
        return
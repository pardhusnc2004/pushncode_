'''
    Leetcode Daily Question (09-11-2024)
    3133. Minimum Array End
    Python3 solution
'''
from typing import List

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        i = 0
        ex = n-1
        iS = []
        res = [0]*64
        for i in range(64):
            if x&(1<<i):
                res[i] = 1
                continue
            iS.append(i)
        n -= 1
        n = bin(n)[2:][::-1]
        i = 0
        while i < len(n):
            res[iS[i]] = int(n[i])
            i += 1
        ans = 0
        for i in range(64):
            if res[i]:
                ans = ans|(1<<i)

        return ans
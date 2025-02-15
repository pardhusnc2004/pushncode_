'''
    Leetcode Daily Question (15-02-2025)
    2698. Find the Punishment Number of an Integer
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def punishmentNumber(self, n: int) -> int:
        def good(n):
            string = str(n*n)
            l = len(string)
            
            def helper(i, cur):
                # print(string, cur)
                if i == l:
                    return cur == n
                tmp = ""
                for k in range(i, l):
                    tmp += string[k]
                    if helper(k+1, cur+int(tmp)):
                        return True
                return False
            res = helper(0, 0)
            # print(n, res)
            return res
        
        res = 0
        for i in range(1, n+1):
            if good(i):
                # print(i)
                res += i*i

        return res
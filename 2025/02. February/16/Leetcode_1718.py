'''
    Leetcode Daily Question (16-02-2025)
    1718. Construct the Lexicographically Largest Valid Sequence
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        N = 2*n-1
        ds = [-1]*N
        vis = [0]*(n+1)

        def go(i):
            if i == N:
                return True
            if ds[i] != -1:
                if go(i+1):
                    return True
                return False
            for k in range(n, 0, -1):
                if not vis[k]:
                    if k == 1:
                        ds[i] = 1
                        vis[k] = 1
                        if go(i+1):
                            return True
                        vis[k] = 0
                        ds[i] = -1
                    else:
                        if i+k < N and ds[i+k] == -1:
                            ds[i] = k
                            ds[i+k] = k
                            vis[k] = 1
                            if go(i+1):
                                return True
                            vis[k] = 0
                            ds[i] = -1
                            ds[i+k] = -1
            return False
        go(0)
        return ds
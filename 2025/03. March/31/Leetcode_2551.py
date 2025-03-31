'''
    Leetcode Daily Question (31-03-2025)
    2551. Put Marbles in Bags
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

# class Solution:
#     def putMarbles(self, weights: List[int], k: int) -> int:
#         n = len(weights)

#         @cache
#         def solve(i, rem, cur):
#             if i >= n:
#                 return
#             if rem == 1:
#                 tmp = weights[i] + weights[-1]
#                 res.append(tmp+cur) 
#                 return               
#             if rem:
#                 for j in range(i, n):
#                     tmp = weights[j] + weights[i]
#                     # print(f'tmp {tmp}, (i, j) {(i, j)} cur {cur}')
#                     solve(j+1, rem-1, cur+tmp)
#             return
#         res = []
#         solve(0, k, 0)
#         res.sort()
#         return res[-1]-res[0]

'''

        #       #  #        # # # #
        # #   # #  #        #
        #   #   #  #        # # # #
        #       #  #        #
        #       #  # # # #  # # # #

'''

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        pairWeights = [weights[i] + weights[i + 1] for i in range(n - 1)]
        pairWeights.sort()
        answer = 0
        for i in range(k - 1):
            answer += pairWeights[n - 2 - i] - pairWeights[i]

        return answer
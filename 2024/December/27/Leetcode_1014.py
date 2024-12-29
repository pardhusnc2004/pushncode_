'''
    Leetcode Daily Question (27-12-2024)
    1014. Best Sightseeing Pair
    Python3 solution
'''
from typing import *
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def maxScoreSightseeingPair(self, values):
        n = len(values)
        max_left_score = [0] * n
        max_left_score[0] = values[0]

        max_score = 0

        for i in range(1, n):
            current_right_score = values[i] - i
            max_score = max(max_score, max_left_score[i - 1] + current_right_score)

            current_left_score = values[i] + i
            max_left_score[i] = max(max_left_score[i - 1], current_left_score)

        return max_score  
 
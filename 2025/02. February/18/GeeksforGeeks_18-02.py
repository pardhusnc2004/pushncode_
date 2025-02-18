'''
    GeeksforGeeks Daily Question (18-02-2025)
    K Closest Points to Origin
    Python3 solution
'''

from math import dist
from heapq import *
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Your code here
        res = []
        hp = [(dist([i, j], [0, 0]), (i, j)) for i, j in points]
        heapify(hp)
        while k and hp:
            k -= 1
            _, points = heappop(hp)
            i, j = points
            res.append([i, j])
        return res
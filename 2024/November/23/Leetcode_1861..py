'''
    Leetcode Daily Question (23-11-2024)
    1861. Rotating the Box
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        newbox = [['.']*m for _ in range(n)]
        for i in range(m):
            last = n-1
            for j in range(n-1, -1, -1):
                if box[i][j] == '#':
                    newbox[last][i] = '#'
                    last -= 1
                elif box[i][j] == '*':
                    newbox[j][i] = '*'
                    last = j-1
        
        def rev(i):
            l, r = 0, len(i)-1
            while l < r:
                i[l], i[r] = i[r], i[l]
                l += 1
                r -= 1
        for i in newbox:
            rev(i)
        return newbox
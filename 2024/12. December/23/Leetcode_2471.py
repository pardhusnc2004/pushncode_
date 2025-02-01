'''
    Leetcode Daily Question (23-12-2024)
    2471. Minimum Number of Operations to Sort a Binary Tree by Level
    Python3 solution
'''
from typing import *
from collections import *
from bisect import *
from math import *
from heapq import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        res = 0

        def swaps(tmp):
            res = 0
            n = len(tmp)
            posMap = {tmp[i]:i for i in range(n)}
            sortedTmp = sorted(tmp)
            for i in range(n):
                if sortedTmp[i] != tmp[i]:
                    res += 1
                    pos = posMap[sortedTmp[i]]
                    posMap[tmp[i]] = pos
                    tmp[pos] = tmp[i]
            return res

        q = deque([root])
        while q:
            tmp = []
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                tmp.append(node.val)
            res += swaps(tmp)
        return res
 
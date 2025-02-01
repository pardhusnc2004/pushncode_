'''
    Leetcode Daily Question (25-12-2024)
    515. Find Largest Value in Each Tree Row
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
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            sz = len(q)
            maxi = -1e16
            for i in range(sz):
                curnode = q.popleft()
                maxi = max(maxi, curnode.val)
                if curnode.left:
                    q.append(curnode.left)
                if curnode.right:
                    q.append(curnode.right)
            res.append(maxi)
        return res
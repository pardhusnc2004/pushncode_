'''
    Leetcode Daily Question (20-12-2024)
    2415. Reverse Odd Levels of Binary Tree
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
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        bfs = []
        q = deque([root])
        idx = 0
        while q:
            tmp = []
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                tmp.append(node.val)
            if idx&1:
                tmp.reverse()
            bfs.append(tmp)
            idx ^= 1
        dummy = TreeNode(bfs[0][0])
        q = deque([dummy])
        for i in range(1, len(bfs)):
            for j in range(0, len(bfs[i]), 2):
                parent = q.popleft()
                leftNode, rightNode = TreeNode(bfs[i][j]), TreeNode(bfs[i][j+1])
                parent.left = leftNode
                parent.right = rightNode
                q.append(leftNode)
                q.append(rightNode)
        return dummy
'''
    Leetcode Daily Question (22-02-2025)
    1028. Recover a Tree From Preorder Traversal
    Python3 solution
'''
from typing import *
from collections import *
from bisect import *
from math import *
from heapq import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        i = 0
        root = None
        n = len(traversal)

        d = defaultdict(list)

        while i < n:
            j = i
            cur = 0
            depth = 0
            if root:
                while j < n and traversal[j] == '-':
                    depth += 1
                    j += 1
            while j < n and traversal[j].isdigit():
                cur = cur*10+int(traversal[j])
                j += 1
            if not root:
                root = TreeNode(cur)
                d[0].append(root)
                # print(d[0])
            else:
                prevLast = d[depth-1][-1]
                newNode = TreeNode(cur)
                if not prevLast.left:
                    prevLast.left = newNode
                else:
                    prevLast.right = newNode
                d[depth].append(newNode)
            # print(i, j)
            i = j
        
        # print(d)
        return d[0][-1]
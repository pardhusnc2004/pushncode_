'''
    Leetcode Daily Question (23-10-2024)
    2641. Cousins in Binary Tree II
    Python3 solution
'''
from typing import Optional
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        d = defaultdict(lambda: defaultdict(list))
        d[0][0] = [root.val]
        temp = root
        q = [temp]
        level = 0
        while q:
            sz = len(q)
            for i in range(sz):
                curnode = q.pop(0)
                if curnode.left:
                    d[level+1][i].append(curnode.left.val)
                    q.append(curnode.left)
                if curnode.right:
                    d[level+1][i].append(curnode.right.val)
                    q.append(curnode.right)
            level += 1
        keySet = list(sorted(d.keys()))
        temp = root
        q = [temp]
        level = 1
        while q:
            sz = len(q)
            levelSum = 0
            for k in d[level]:
                levelSum += sum(d[level][k])
            for i in range(sz):
                curnode = q.pop(0)
                if curnode.left:
                    q.append(curnode.left)
                    curnode.left.val = levelSum - sum(d[level][i])
                if curnode.right:
                    q.append(curnode.right)
                    curnode.right.val = levelSum - sum(d[level][i])
            level += 1
        root.val = 0
        return root
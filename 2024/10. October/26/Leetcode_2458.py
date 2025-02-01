'''
    Leetcode Daily Question (26-10-2024)
    2458. Height of Binary Tree After Subtree Removal Queries
    Python3 solution
'''
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        def solve(curnode, queryNodeVal):
            if curnode is None or curnode.val == queryNodeVal:
                return 0
            left, right = solve(curnode.left, queryNodeVal), solve(curnode.right, queryNodeVal)
            return 1+max(left, right)
        res = []
        for queryNodeVal in queries:
            res.append(solve(root, queryNodeVal)-1)
        return res
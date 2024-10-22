'''
    Leetcode Daily Question (22-10-2024)
    2583. Kth Largest Sum in a Binary Tree
    Python3 solution
'''
from heapq import heappush, heappop
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        hp = []
        q = [root]
        while q:
            sz = len(q)
            cursum = 0
            for i in range(sz):
                curnode = q.pop(0)
                cursum += curnode.val
                if curnode.left:
                    q.append(curnode.left)
                if curnode.right:
                    q.append(curnode.right)
            heappush(hp, -cursum)
        if len(hp) < k:
            return -1
        k -= 1
        while k:
            heappop(hp)
            k -= 1
        return -heappop(hp)
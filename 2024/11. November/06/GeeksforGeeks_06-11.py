'''
    GeeksforGeeks Daily Question (06-11-2024)
    Root to leaf paths sum
    Python3 solution
'''

class Solution:
    def treePathSum(self,root):
        # Code here
        res = [0]
        def solve(root, cur):
            nonlocal res
            if not root:
                return
            if not root.left and not root.right:
                res[0] += cur*10+root.data
                return
            solve(root.left, cur*10+root.data)
            solve(root.right, cur*10+root.data)
            return
        solve(root, 0)
        return res[0]
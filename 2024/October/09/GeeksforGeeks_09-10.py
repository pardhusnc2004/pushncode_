'''
    GeeksforGeeks Daily Question (09-10-2024)
    Linked List Matrix
    Python3 solution
'''

class Node():
    def __init__(self,x):
        self.data = x
        self.right = None
        self.down=None

class Solution:
    def constructUtil(self, mat, i, j, m, n):
        if i >= n or j >= m:
            return None

        temp = Node(mat[i][j])
        temp.right = self.constructUtil(mat, i, j + 1, m, n)
        temp.down = self.constructUtil(mat, i + 1, j, m, n)
        return temp

    def constructLinkedMatrix(self, mat):
        n = len(mat)
        m = len(mat[0])
        return self.constructUtil(mat, 0, 0, m, n)
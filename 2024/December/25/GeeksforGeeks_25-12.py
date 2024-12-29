'''
    GeeksforGeeks Daily Question (25-12-2024)
    Set Matrix Zeroes
    Python3 solution
'''

class Solution:
    def setMatrixZeroes(self, mat):
        m, n = len(mat), len(mat[0])
        rows, cols = [0]*m, [0]*n
        for i in range(m):
            for j in range(n):
                if not mat[i][j]:
                    cols[j] = 1
                    rows[i] = 1
                    
        for i in range(m):
            for j in range(n):
                if rows[i] or cols[j]:
                    mat[i][j] = 0

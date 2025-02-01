'''
    GeeksforGeeks Daily Question (20-12-2024)
    Spirally traversing a matrix
    Python3 solution
'''

class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, mat):
        r = len(mat)
        c = len(mat[0])
        res = []

        row = 0
        col = 0

        while row < r and col < c:
            for i in range(col, c):
                res.append(mat[row][i])
            row += 1
            
            for i in range(row, r):
                res.append(mat[i][c - 1])
            c -= 1

            if row < r:
                for i in range(c - 1, col - 1, -1):
                    res.append(mat[r - 1][i])
                r -= 1

            if col < c:
                for i in range(r - 1, row - 1, -1):
                    res.append(mat[i][col])
                col += 1

        return res
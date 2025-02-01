'''
    GeeksforGeeks Daily Question (31-01-2025)
    Solve the Sudoku
    Python3 solution
'''

class Solution:
    
    #Function to find a solved Sudoku. 
    def solveSudoku(self, mat):
        
        # Your code here
        def valid(n, r, c):
            for i in range(9):
                if mat[i][c] == n or mat[r][i] == n:
                    return False
            bi, bj = r//3, c//3
            bi *= 3
            bj *= 3
            for a in range(3):
                for b in range(3):
                    ta, tb = bi+a, bj+b
                    if mat[ta][tb] == n:
                        return False
            return True
        rem = []
        for i in range(9):
            for j in range(9):
               if mat[i][j] == 0:
                   rem.append((i, j))
        def solve(i):
            if i == len(rem):
                return True
            r, c = rem[i]
            for k in range(1, 10):
                if valid(k, r, c):
                    mat[r][c] = k
                    if solve(i+1):
                        return True
                    mat[r][c] = 0
            return False
        solve(0)
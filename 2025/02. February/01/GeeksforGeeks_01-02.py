'''
    GeeksforGeeks Daily Question (01-02-2025)
    Word Search
    Python3 solution
'''

class Solution:
    def isWordExist(self, mat, word):
        #Code here
        m, n = len(mat), len(mat[0])
        l = len(word)
        dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
        def solve(i, r, c):
            if i == l:
                return True
            for k in range(4):
                nr, nc = r+dx[k], c+dy[k]
                if 0 <= nr < m and 0 <= nc < n:
                    if word[i] == mat[nr][nc]:
                        mat[nr][nc] = '?'
                        if solve(i+1, nr, nc):
                            return True
                        mat[nr][nc] = word[i]
            return False
        for i in range(m):
            for j in range(n):
                if word[0] == mat[i][j]:
                    mat[i][j] = '?'
                    if solve(1, i, j):
                        return True
                    mat[i][j] = word[0]
        return False


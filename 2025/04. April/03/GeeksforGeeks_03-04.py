'''
    GeeksforGeeks Daily Question (03-04-2025)
    Rotten Oranges
    Python3 solution
'''

class Solution:

    #Function to find minimum time required to rot all oranges. 
    def orangesRotting(self, grid):
        #Code here
        q = []
        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
        twos = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append([0, i, j])
                elif grid[i][j]:
                    twos += 1
        res = 0
        ones = 0
        while q:
            sz = len(q)
            for _ in range(sz):
                curtime, r, c = q.pop(0)
                for k in range(4):
                    nr, nc = r+dx[k], c+dy[k]
                    if nr>=0 and nc>=0 and nr<m and nc<n and grid[nr][nc] == 1:
                        ones += 1
                        grid[nr][nc] = 2
                        res = max(res, curtime+1)
                        q.append([curtime+1, nr, nc])
            if ones == twos:
                return res
        if ones != twos:
            return -1
        return res

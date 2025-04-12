'''
    GeeksforGeeks Daily Question (12-04-2025)
    Flood fill Algorithm
    Python3 solution
'''

from collections import deque

class Solution:
    def floodFill(self, image, sr, sc, newColor):
        #Code here
        m, n = len(image), len(image[0])
        dij = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        if image[sr][sc] == newColor:
            return image
        
        q = deque([(sr, sc)])
        vis = set([(sr, sc)])
        while q:
            i, j = q.popleft()
            tmpColor = image[i][j]
            image[i][j] = newColor
            for di, dj in dij:
                ni, nj = i+di, j+dj
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in vis and image[ni][nj] == tmpColor:
                    q.append((ni, nj))
                    vis.add((ni, nj))
        
        return image

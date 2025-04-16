'''
    GeeksforGeeks Daily Question (16-04-2025)
    Floyd Warshall
    Python3 solution
'''

#User function template for Python

class Solution:
    def floydWarshall(self, dist):
        #Code here
        inf = 10**8
        n = len(dist)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        return dist
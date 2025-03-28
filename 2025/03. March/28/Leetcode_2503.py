'''
    Leetcode Daily Question (28-03-2025)
    2503. Maximum Number of Points From Grid Queries
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n, k = len(grid), len(grid[0]), len(queries)
        maxGrid = max(max(row) for row in grid)

        dij = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        hp = [(grid[0][0], 0, 0)]
        vis = set()
        

        res = [0]*k
        queries = sorted([(queries[i], i) for i in range(k)])
        for q, idx in queries:
            while hp and hp[0][0] < q:
                # print(hp)
                _, curi, curj = heappop(hp)
                vis.add((curi, curj))
                for di, dj in dij:
                    ni, nj = curi+di, curj+dj
                    if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in vis:
                        # vis.add((ni, nj))
                        heappush(hp, (grid[ni][nj], ni, nj))
            res[idx] = len(vis)
        return res
    
'''
    PYTHON3 Solution might not AC, refer to JAVA code


    class Solution {
        class GridItem {
            int wt, i, j;
            public GridItem(int wt, int i, int j) {
                this.wt = wt;
                this.i = i;
                this.j = j;
            }
        }
        public int[] maxPoints(int[][] grid, int[] queries) {
            PriorityQueue<GridItem> pq = new PriorityQueue<>((a, b) -> a.wt - b.wt);
            int ql = queries.length;
            int res[] = new int[ql];
            int m = grid.length;
            int n = grid[0].length;
            int vis[][] = new int[m][n];
            int total = 0;

            List<List<Integer>> querys = new ArrayList<>();
            for(int i=0; i<ql; i++) {
                List<Integer> tmp = new ArrayList<>();
                tmp.add(queries[i]);
                tmp.add(i);
                querys.add(tmp);
            }

            querys.sort(Comparator.comparingInt(a -> a.get(0)));
            int di[] = new int[] {1, 0, -1, 0};
            int dj[] = new int[] {0, -1, 0, 1};

            pq.offer(new GridItem(grid[0][0], 0, 0));

            for(List<Integer> lst: querys) {
                while(!pq.isEmpty() && pq.peek().wt < lst.get(0)) {
                    GridItem item = pq.poll();
                    vis[item.i][item.j] = 1;
                    total += 1;

                    for(int k=0; k<4; k++) {
                        int ni = item.i + di[k];
                        int nj = item.j + dj[k];
                        if(ni >= 0 && ni < m && nj >= 0 && nj < n && vis[ni][nj] == 0) {
                            vis[ni][nj] = 1;
                            pq.offer(new GridItem(grid[ni][nj], ni, nj));
                        }
                    }
                }
                res[lst.get(1)] = total;
            }
            return res;
        }
    }
'''
'''
    Leetcode Daily Question (11-10-2024)
    1942. The Number of the Smallest Unoccupied Chair
    Python3 solution
'''

from typing import List
from heapq import heappop, heappush

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        q = []
        arrival_target = times[targetFriend][0]
        times.sort()
        avail = [i for i in range(10**4)]
        # print(times)
        for i in range(len(times)):
            while q and q[0][0] <= times[i][0]:
                poss = heappop(q)
                heappush(avail, poss[1])
            cur = heappop(avail)
            heappush(q, [times[i][-1], cur])
            if times[i][0] == arrival_target:
                return cur
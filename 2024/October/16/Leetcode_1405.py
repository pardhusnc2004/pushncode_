'''
    Leetcode Daily Question (16-10-2024)
    1405. Longest Happy String
    Python3 solution
'''

from heapq import heapify, heappop, heappush

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        hp = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        heapify(hp)
        res = "--"
        
        while hp:
            rem, alpha = heappop(hp)
            # print(rem, alpha, "first")
            if not rem:
                continue
            if res[-1] != alpha:
                res += alpha
                heappush(hp, (-(abs(rem)-1), alpha))
            else:
                if res[-2] != alpha:
                    res += alpha
                    heappush(hp, (-(abs(rem)-1), alpha))

                else:
                    if not hp:
                        break
                    r2, a2 = heappop(hp)
                    # print(r2, a2, "second")
                    if not r2:
                        continue
                    res += a2
                    heappush(hp, (-(abs(r2)-1), a2))
                    heappush(hp, (-(abs(rem)), alpha))

        return res[2:]
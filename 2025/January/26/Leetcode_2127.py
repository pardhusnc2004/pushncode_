'''
    Leetcode Daily Question (26-01-2025)
    2127. Maximum Employees to Be Invited to a Meeting
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

'''
    A company is organizing a meeting and has a list of n employees, waiting to be invited. They have arranged for a large circular table, capable of seating any number of employees.

    The employees are numbered from 0 to n - 1. Each employee has a favorite person and they will attend the meeting only if they can sit next to their favorite person at the table. The favorite person of an employee is not themself.

    Given a 0-indexed integer array favorite, where favorite[i] denotes the favorite person of the ith employee, return the maximum number of employees that can be invited to the meeting.

    It seemed pretty difficult for me at beginning, watched some solutions and tutorials to get through this question.
'''

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        N = len(favorite)

        r = defaultdict(set)
        for index, x in enumerate(favorite):
            r[x].add(index)

        vis = [False] * N
        def go(x):
            vis[x] = True
            mx = 0
            for v in r[x]:
                mx = max(mx, go(v) + 1)
            return mx

        res = 0
        for i in range(N):
            if i < favorite[i] and favorite[favorite[i]] == i:
                r[i].remove(favorite[i])
                r[favorite[i]].remove(i)

                maxLeft = go(i)
                maxRight = go(favorite[i])

                res += 2 + maxLeft + maxRight
        
        for i in range(N):
            if not vis[i]:
                pathVis = {}

                step = 0
                current = i
                good = True
                while current not in pathVis:
                    if vis[current]:
                        good = False
                        break
                    vis[current] = True
                    pathVis[current] = step
                    step += 1
                    current = favorite[current]

                if good:
                    cycle = step - pathVis[current]
                    res = max(res, cycle)
        
        return res


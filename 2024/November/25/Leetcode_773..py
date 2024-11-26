'''
    Leetcode Daily Question (25-11-2024)
    773. Sliding Puzzle
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class HeapThing:
    def __init__(self, dist, step, ds):
        self.dist = dist
        self.step = step
        self.ds = ds
    def __lt__(self, thing):
        if self.step == thing.step:
            return self.dist < thing.dist 
        return self.step < thing.step

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def getHeuristic(n, i, j):
            ri, rj = (n-1)//3, (n-1)%3
            return abs(i-ri)+abs(j-rj)
        def getStateHeuristic(brd):
            hs = 0
            for i in range(2):
                for j in range(3):
                    if brd[i][j] > 0:
                        hs += getHeuristic(brd[i][j], i, j)
                    else:
                        hs += (1-i)+(2-j)
            return hs
        hp = [HeapThing(getStateHeuristic(board), 0, board)]
        def copy(brd):
            ns = []
            for row in brd:
                ns.append(row[:]+[])
            return ns
        def getPossibleChanges(brd):
            ei, ej = 0, 0
            for i in range(2):
                for j in range(3):
                    if brd[i][j] == 0:
                        ei, ej = i, j
                        break
            # print(ei, ej)
            poss = []
            if ei-1 >= 0:
                up = brd[ei-1][ej]
                brd[ei-1][ej] = 0
                brd[ei][ej] = up
                poss.append(copy(brd))
                brd[ei][ej] = 0
                brd[ei-1][ej] = up
            if ei+1 < 2:
                down = brd[ei+1][ej]
                brd[ei+1][ej] = 0
                brd[ei][ej] = down
                poss.append(copy(brd))
                brd[ei][ej] = 0
                brd[ei+1][ej] = down
            if ej-1 >= 0:
                left = brd[ei][ej-1]
                brd[ei][ej-1] = 0
                brd[ei][ej] = left
                poss.append(copy(brd))
                brd[ei][ej] = 0
                brd[ei][ej-1] = left
            if ej+1 < 3:
                right = brd[ei][ej+1]
                brd[ei][ej+1] = 0
                brd[ei][ej] = right
                poss.append(copy(brd))
                brd[ei][ej] = 0
                brd[ei][ej+1] = right
            return poss
        def getStateTuple(brd):
            tup = ""
            for row in brd:
                tup += "".join(list(map(str, brd)))
            return tup
        seen = set()
        res = inf
        while hp:
            hpThing = heappop(hp)
            curDist, curStep, curState = hpThing.dist, hpThing.step, hpThing.ds
            # print(curDist, curStep, curState)
            if curDist == 0:
                res = min(res, curStep)
                continue
            poss = getPossibleChanges(curState)
            # print(poss)
            for p in poss:
                if getStateTuple(p) not in seen:
                    seen.add(getStateTuple(p))
                    heappush(hp, HeapThing(getStateHeuristic(p), curStep+1, p))

        return res if res != inf else -1

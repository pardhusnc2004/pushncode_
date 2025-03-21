'''
    Leetcode Daily Question (21-03-2025)
    2115. Find All Possible Recipes from Given Supplies
    Python3 solution
'''
from typing import *
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        n = len(recipes)
        dMap = {recipes[i]:i for i in range(n)}
        res = []
        vis = set()

        def dfs(i):
            vis.add(i)
            flag = 1
            for k in ingredients[i]:
                if k not in supplies:
                    if k not in dMap:
                        flag = 0
                        break
                    else:
                        if dMap[k] not in vis and dfs(dMap[k]):
                            continue
                        flag = 0
                        break
            if flag:
                supplies.add(recipes[i])
            return flag

        for i in range(n):
            if dfs(i):
                res.append(recipes[i])
        return res
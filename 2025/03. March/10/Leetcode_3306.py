'''
    Leetcode Daily Question (10-03-2025)
    3306. Count of Substrings Containing Every Vowel and K Consonants II
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def helper(kk):
            res, left, dv, conso = 0, 0, {}, 0
            n = len(word)
            for right in range(n):
                if word[right] in "aeiou":
                    dv[word[right]] = dv.get(word[right], 0)+1
                else:
                    conso += 1
                while len(dv) == 5 and conso >= kk:
                    res += (n-right) #+1
                    if word[left] in "aeiou":
                        dv[word[left]] -= 1
                        if not dv[word[left]]:
                            del dv[word[left]]
                    else:
                        conso -= 1
                    left += 1
                # print(right, left, res, dv, conso)
            # print("NEXT")
            return res
        a, b = helper(k), helper(k+1)
        # print(a, b)
        return a - b
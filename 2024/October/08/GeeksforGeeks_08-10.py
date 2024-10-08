'''
    GeeksforGeeks Daily Question (08-10-2024)
    Largest Pair Sum
    Python3 solution
'''
from typing import List

class Solution:
    def pairsum(self, arr : List[int]) -> int:
        # code here
        return sum(list(sorted(arr))[-2:])
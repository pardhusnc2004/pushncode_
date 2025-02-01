'''
    Leetcode Daily Question (07-11-2024)
    2275. Largest Combination With Bitwise AND Greater Than Zero
    Python3 solution
'''
from typing import List

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        nums = [0]*32
        for i in candidates:
            # k = bin(i)[2:]
            # print('0'*(32-len(k))+k)
            for j in range(32):
                if i&(1<<j):
                    nums[j] += 1
        # print(nums)

        return max(nums)
'''
    Leetcode Daily Question (18-10-2024)
    2044. Count Number of Maximum Bitwise-OR Subsets
    Python3 solution
'''

from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOr = 0
        for i in nums:
            maxOr |= i
        
        res = 0
        for i in range(1<<(len(nums))):
            cr = 0
            for j in range(len(nums)):
                if i&(1<<j):
                    cr |= nums[j]
            if cr == maxOr:
                res += 1

        return res
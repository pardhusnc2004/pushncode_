'''
    Leetcode Daily Question (06-11-2024)
    3011. Find if Array Can Be Sorted
    Python3 solution
'''
from typing import List

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        def getbits(n):
            ctr = 0
            while(n):
                if n&1:
                    ctr+=1
                n = n>>1
            return ctr
        d = {}
        for i in nums:
            if i not in d:
                d[i] = getbits(i)
        for i in range(n):
            for j in range(n):
                if d[nums[j]] == d[nums[j-1]]:
                    if j and nums[j] < nums[j-1]:
                        nums[j], nums[j-1] = nums[j-1], nums[j]
        return sorted(nums) == nums
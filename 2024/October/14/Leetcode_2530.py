'''
    Leetcode Daily Question (14-10-2024)
    2530. Maximal Score After Applying K Operations
    Python3 solution
'''

from typing import List
import heapq
import math

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        for i,n in enumerate(nums):
            nums[i] = -n
        heapq.heapify(nums)
        res = 0
        while nums and k:
            num = -heapq.heappop(nums)
            k-=1
            res += num
            heapq.heappush(nums, -math.ceil(num/3))
        return res
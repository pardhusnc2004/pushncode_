'''
    Leetcode Daily Question (30-10-2024)
    1671. Minimum Number of Removals to Make Mountain Array
    Python3 solution
'''
from typing import List, Optional

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        inc, dec = [1]*n, [1]*n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    inc[i] = max(inc[i], 1+inc[j])
        for i in range(n-2, -1, -1):
            for j in range(n-1, i, -1):
                if nums[i] > nums[j]:
                    dec[i] = max(dec[i], 1+dec[j])
        maxi = 0
        # print(inc, dec)
        for i in range(n):
            if inc[i] > 1 and dec[i] > 1:
                maxi = max(maxi, inc[i]+dec[i]-1)
        res = n - maxi
        return res if maxi >= 3 else 0
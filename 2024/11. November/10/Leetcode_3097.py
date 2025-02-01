'''
    Leetcode Daily Question (10-11-2024)
    3097. Shortest Subarray With OR at Least K II
    Python3 solution
'''
from typing import List

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        bits = [0]*33
        left = 0
        res = 1e10
        reqBits = [0]*33
        for kk in range(33):
            if k&(1<<kk):
                reqBits[kk] += 1
        
        def poss(bits):
            getK = 0
            for i in range(33):
                if bits[i]:
                    getK |= (1<<i)
            # print(getK, k)
            return getK >= k

        n = len(nums)
        cur = 0
        for right in range(n):
            for kk in range(32):
                if nums[right]&(1<<kk):
                    bits[kk] += 1
            while left <= right and poss(bits):
                res = min(res, right-left+1)
                for kk in range(33):
                    if nums[left]&(1<<kk):
                        bits[kk] -= 1
                left += 1

        return res if res != 1e10 else -1
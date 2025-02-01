'''
    Leetcode Daily Question (11-11-2024)
    2601. Prime Subtraction Operation
    Python3 solution
'''
from typing import List

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        sE = [1]*(1001)
        for i in range(2, 1001):
            if not sE[i]:
                continue
            for j in range(i*i, 1001, i):
                sE[j] = 0
        primes = []
        for i in range(2, 1001):
            if sE[i]:
                primes.append(i)
        n = len(nums)
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                continue
            for p in primes:
                if nums[i] > p and nums[i]-p < nums[i+1]:
                    nums[i] -= p
                    break
            if nums[i] >= nums[i+1]:
                return False
        return True

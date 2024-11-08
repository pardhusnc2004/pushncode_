'''
    Leetcode Daily Question (08-11-2024)
    1829. Maximum XOR for Each Query
    Python3 solution
'''
from typing import List

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        def getK(bits):
            res = 0
            for i in range(maximumBit):
                if bits&(1<<i):
                    continue
                else:
                    res |= (1<<i)
            return res
            pass

        bits = 0
        res = []
        for i in nums:
            bits ^= i
            res.append(getK(bits))
        return res[::-1]
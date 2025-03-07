'''
    Leetcode Daily Question (07-03-2025)
    2523. Closest Prime Numbers in Range
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:

    def __init__(self):
        self.sieve_ = [1]*(10**6+2)
        self.n = 10**6+2
        self.primes = []
        self.soe_()
    
    def soe_(self):
        self.sieve_[0] = self.sieve_[1] = 0
        for i in range(2, self.n):
            if self.sieve_[i]:
                self.primes.append(i)
                for j in range(i*i, self.n, i):
                    self.sieve_[j] = 0

    def closestPrimes(self, left: int, right: int) -> List[int]:
        _leftIndex = bisect_left(self.primes, left)
        _rightIndex = bisect_left(self.primes, right+1)
        res = [-inf, inf]
        # print(_leftIndex, _rightIndex)
        # print(self.primes[_leftIndex:_rightIndex+1])
        for i in range(_leftIndex, _rightIndex-1):
            if res[1]-res[0] > (self.primes[i+1]-self.primes[i]):
                res = [self.primes[i], self.primes[i+1]]    

        return res if res != [-inf, inf] else [-1, -1]
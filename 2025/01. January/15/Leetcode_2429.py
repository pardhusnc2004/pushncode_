'''
    Leetcode Daily Question (15-01-2025)
    2429. Minimize XOR
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        res = 0
        def setBits(n):
            res = 0
            while n:
                n &= (n-1)
                res += 1
            return res
        bits1, bits2 = setBits(num1), setBits(num2)
        
        if bits1 == bits2:
            return num1
        
        elif bits1 > bits2:
            num1, num2 = bin(num1)[2:], bin(num2)[2:]
            tmp = ""
            for i in num1:
                if i == '1':
                    if bits2:
                        bits2 -= 1
                        tmp += '1'
                    else:
                        tmp += '0'
                else:
                    tmp += '0'
            return int(tmp, 2)
        else:
            num1, num2 = bin(num1)[2:], bin(num2)[2:]
            tmp = ""
            for i in num1:
                if i == '1':
                    bits2 -= 1
                    tmp += '1'
                else:
                    tmp += '0'
            tmp2 = ""
            for i in range(len(tmp)-1, -1, -1):
                if tmp[i] == '0':
                    if bits2:
                        bits2 -= 1
                        tmp2 = '1'+tmp2
                    else:
                        tmp2 = '0'+tmp2
                else:
                    tmp2 = '1'+tmp2
            while bits2:
                tmp2 = '1'+tmp2
                bits2 -= 1
            return int(tmp2, 2)
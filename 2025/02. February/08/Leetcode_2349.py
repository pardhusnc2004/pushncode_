'''
    Leetcode Daily Question (08-02-2025)
    2349. Design a Number Container System
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class NumberContainers:

    def __init__(self):
        self.inMap = {}
        self.numMap = {}

    def change(self, index: int, number: int) -> None:
        if index in self.inMap:
            self.numMap[self.inMap[index]].remove(index)
        self.inMap[index] = number
        if number not in self.numMap:
            self.numMap[number] = set() # use sortedContainers instead of set
        self.numMap[number].add(index)

    def find(self, number: int) -> int:
        if number not in self.numMap or not self.numMap[number]:
            return -1
        return self.numMap[number][0]
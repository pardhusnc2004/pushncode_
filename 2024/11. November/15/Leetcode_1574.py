'''
    Leetcode Daily Question (15-11-2024)
    1574. Shortest Subarray to be Removed to Make Array Sorted
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        res = n
        right = n-1
        while right > 0 and arr[right] >= arr[right-1]:
            right -= 1
        if right == 0:
            return 0
        res = right
        left = 0
        while left < n and (left == 0 or arr[left-1] <= arr[left]):
            while right < n and arr[right] < arr[left]:
                right += 1
            res = min(res, right-left-1)
            left += 1
        return res
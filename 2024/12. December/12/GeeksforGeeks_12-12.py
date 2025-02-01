'''
    GeeksforGeeks Daily Question (12-12-2024)
    Number of occurrence
    Python3 solution
'''

from bisect import *

class Solution:
    def countFreq(self, arr, target):
        #code here
        ub, lb = bisect_right(arr, target), bisect_left(arr, target)
        if lb >= len(arr) or arr[lb] != target:
            return 0
        return ub-lb

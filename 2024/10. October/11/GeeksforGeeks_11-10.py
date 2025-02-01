'''
    GeeksforGeeks Daily Question (10-10-2024)
    Reorganize The Array
    Python3 solution
'''

class Solution:
    def rearrange(self, arr):
        #Code here
        s = set(arr)
        return [-1 if i not in s else i for i in range(len(arr))]
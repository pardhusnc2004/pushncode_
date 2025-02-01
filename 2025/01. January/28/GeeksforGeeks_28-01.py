'''
    GeeksforGeeks Daily Question (28-01-2025)
    Permutations of a String
    Python3 solution
'''

from itertools import permutations

class Solution:
    def findPermutation(self, s):
        # Code here
        res = permutations(list(s))
        return list(set(["".join(i) for i in res]))


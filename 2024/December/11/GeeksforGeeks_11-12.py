'''
    GeeksforGeeks Daily Question (11-12-2024)
    Merge Without Extra Space
    Python3 solution
'''

class Solution:
    def mergeArrays(self, a, b):
        # code here
        m, n = len(a), len(b)
        l, r = m-1, 0
        while l>=0 and r<n:
            if a[l] > b[r]:
                a[l], b[r] = b[r], a[l]
                l -= 1
                r += 1
            else:
                break
        a.sort()
        b.sort()

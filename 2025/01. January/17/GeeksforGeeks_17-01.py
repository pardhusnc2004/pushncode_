'''
    GeeksforGeeks Daily Question (17-01-2025)
    Product array puzzle
    Python3 solution
'''

class Solution:
    def productExceptSelf(self, arr):
        #code here
        pref, suff = [1], [1]
        p = 1
        for i in arr:
            p *= i
            pref.append(p)
        s = 1
        for i in arr[::-1]:
            s *= i
            suff.append(s)
        suff.reverse()
        res = [1]*len(arr)
        for i in range(len(arr)):
            res[i] = pref[i]*suff[i+1]
        return res
'''
    GeeksforGeeks Daily Question (05-01-2025)
    Count Pairs whose sum is less than target
    Python3 solution
'''

class Solution:
    #Complete the below function 1 2 2 3 4 5
    def countPairs(self, arr, target):
        #Your code here
        arr.sort()
        n = len(arr)
        res = 0
        # print(arr)
        for i in range(n):
            l, r = i+1, n
            tmp = i
            while l < r:
                m = (l+r) >> 1
                if arr[i]+arr[m] < target:
                    tmp = m
                    l = m+1
                else:
                    r = m
            # print(i, tmp)
            res += (tmp-i)
        return res

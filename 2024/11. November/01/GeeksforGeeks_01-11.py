'''
    GeeksforGeeks Daily Question (01-11-2024)
    Swap and Maximize
    Python3 solution
'''

class Solution:
    def maxSum(self,arr):
        # code here
        arr.sort()
        narr = []
        n = len(arr)
        i, j = 0, len(arr)-1
        while i < j:
            narr.append(arr[i])
            narr.append(arr[j])
            i += 1
            j -= 1
        if i <= j:
            narr.append(arr[i])
        res = abs(narr[-1]-narr[0])
        # print(res)
        for i in range(n-1):
            res += abs(narr[i]-narr[i+1])
            # print(res)
        return res
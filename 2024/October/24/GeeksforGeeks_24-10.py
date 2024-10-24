'''
    GeeksforGeeks Daily Question (24-10-2024)
    Modify the Array
    Python3 solution
'''

class Solution:
    def modifyAndRearrangeArr (self, arr) : 
        #Complete the function
        i, j = 0, 1
        if len(arr) == 1:
            return arr
        while j < len(arr):
            if arr[i] == arr[j]:
                arr[i] = 0
                arr[j] *= 2
            i += 1
            j += 1
        res = []
        z = 0
        for i in arr:
            if not i:
                z += 1
            else:
                res.append(i)
        for _ in range(z):
            res.append(0)
        return res
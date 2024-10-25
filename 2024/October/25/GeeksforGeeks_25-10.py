'''
    GeeksforGeeks Daily Question (25-10-2024)
    Alternative Sorting
    Python3 solution
'''

class Solution:
    def alternateSort(self,arr):
        # Your code goes here
        res = []
        arr.sort()
        i, j = 0, len(arr)-1
        while i < j:
            res.append(arr[j])
            res.append(arr[i])
            i += 1
            j -= 1
        if i <= j:
            res.append(arr[i])
        return res
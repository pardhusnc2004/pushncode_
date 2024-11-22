'''
    GeeksforGeeks Daily Question (17-11-2024)
    Reverse an Array
    Python3 solution
'''

class Solution:
    def reverseArray(self, arr):
        # code here
        i, j = 0, len(arr)-1
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        return arr
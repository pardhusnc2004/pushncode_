'''
    GeeksforGeeks Daily Question (05-12-2024)
    Sort 0s, 1s and 2s
    Python3 solution
'''

class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # code here
        n = len(arr)
        i, j, k = 0, 0, n-1
        while j <= k:
            if arr[j] == 0:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j += 1
            elif arr[j] == 1:
                j += 1
            else:
                arr[j], arr[k] = arr[k], arr[j]
                k -= 1
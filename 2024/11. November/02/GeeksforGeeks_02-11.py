'''
    GeeksforGeeks Daily Question (02-11-2024)
    Kth distance
    Python3 solution
'''

class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        # your code
        seen = {}
        for i in range(len(arr)):
            if arr[i] in seen:
                if i-seen[arr[i]] <= k:
                    return True
            seen[arr[i]] = i
        return False
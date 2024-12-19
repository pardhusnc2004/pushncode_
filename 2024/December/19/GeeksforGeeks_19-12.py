'''
    GeeksforGeeks Daily Question (19-12-2024)
    Kth Missing Positive Number in a Sorted Array
    Python3 solution
'''

class Solution:
    def kthMissing(self, arr, k):
        # code here
        k -= 1
        s = set(arr)
        for i in range(1, 10**6+1):
            if i not in s:
                if not k:
                    return i
                k -= 1
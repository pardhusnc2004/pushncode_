'''
    GeeksforGeeks Daily Question (27-10-2024)
    Triplet Family
    Python3 solution
'''

class Solution:
    def findTriplet(self, arr):
        n = len(arr)
        arr.sort()
        for i in range(n-1, 1, -1):
            target = arr[i]
            d = {}
            for j in range(i):
                if target-arr[j] in d:
                    return True
                d[arr[j]] = d.get(arr[j], 0)+1
        return False
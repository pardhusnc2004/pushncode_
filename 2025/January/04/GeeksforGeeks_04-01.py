'''
    GeeksforGeeks Daily Question (04-01-2025)
    Count all triplets with given sum in sorted array
    Python3 solution
'''

from collections import defaultdict
class Solution:
    def countTriplets(self, arr, target):
        m = defaultdict(int)
        for e in arr:
            m[e] += 1
        
        ans = 0
        for i in range(len(arr)):
            m[arr[i]] -= 1         
            for j in range(0, i): 
                lookfor = target-arr[i]-arr[j]
                ans += m[lookfor]
        return ans
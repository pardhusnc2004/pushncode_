'''
    GeeksforGeeks Daily Question (16-03-2025)
    Minimum Jumps
    Python3 solution
'''

class Solution:
	def minJumps(self, arr):
	    # code here
            cur = 0
            maxreach = 0
            res = 0
            for i in range(len(arr)-1):
                  maxreach = max(maxreach, i+arr[i])
                  if i == cur:
                        res += 1
                        cur = maxreach
            return -1 if cur < len(arr)-1 else res
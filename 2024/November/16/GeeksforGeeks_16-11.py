'''
    GeeksforGeeks Daily Question (16-11-2024)
    Move All Zeroes to End
    Python3 solution
'''

class Solution:
	def pushZerosToEnd(self,arr):
    	# code here
         n = len(arr)
         i = 0
         left = 0
         while i < n:
            if arr[i] == 0:
                i += 1
                continue
            else:
                arr[left] = arr[i]
                left += 1
            i += 1
         while left < n:
            arr[left] = 0
            left += 1
         return arr
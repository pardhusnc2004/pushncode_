'''
    GeeksforGeeks Daily Question (24-12-2024)
    Search in a sorted Matrix
    Python3 solution
'''

class Solution:
	def searchMatrix(self, mat, x):
		for row in mat:
			if x in row:
				return True
		return False
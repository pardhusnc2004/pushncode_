'''
    GeeksforGeeks Daily Question (22-12-2024)
    Search in a Row-Column sorted matrix
    Python3 solution
'''

class Solution:
	def matSearch(self, mat, x):
		for row in mat:
			if x in row:
				return True
		return False
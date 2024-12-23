'''
    GeeksforGeeks Daily Question (23-12-2024)
    Search in a row-wise sorted matrix
    Python3 solution
'''

class Solution:
	def searchRowMatrix(self, mat, x):
		for row in mat:
			if x in row:
				return True
		return False
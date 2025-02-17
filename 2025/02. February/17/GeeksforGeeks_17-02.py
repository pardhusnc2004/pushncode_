'''
    GeeksforGeeks Daily Question (17-02-2025)
    k largest elements
    Python3 solution
'''

from heapq import heapify, heappop

class Solution:
	def kLargest(self, arr, k):
		hp = [-i for i in arr]
		heapify(hp)
		res = []
		while k and hp:
			k -= 1
			res.append(-heappop(hp))
		return res
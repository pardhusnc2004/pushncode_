'''
    GeeksforGeeks Daily Question (20-02-2025)
    Find median in a stream
    Python3 solution
'''

from heapq import *
class Solution:
    def getMedian(self, arr):
        minheap, maxheap = [], []
        res = []
        def add(i):
            if not maxheap or i <= -maxheap[0]:
                heappush(maxheap, -i)
            else:
                heappush(minheap, i)
            if len(maxheap) > len(minheap)+1:
                heappush(minheap, -heappop(maxheap))
            elif len(minheap) > len(maxheap):
                heappush(maxheap, -heappop(minheap))
            
        def find():
            if len(maxheap) > len(minheap):
                return -maxheap[0]
            return (minheap[0]-maxheap[0])/2.0
        
        for i in arr:
            add(i)
            res.append(find())
        return res
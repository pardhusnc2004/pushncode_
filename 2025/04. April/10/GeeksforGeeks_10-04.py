'''
    GeeksforGeeks Daily Question (10-04-2025)
    Minimum cost to connect all houses in a city
    Python3 solution
'''

#User function Template for python3
import heapq
class Solution:
    def minCost(self, houses):
        n=len(houses)
        visited=set()
        minHeap=[(0,0)]
        totalCost=0
        
        while len(visited)<n:
            cost,curr=heapq.heappop(minHeap)
            if curr in visited:
                continue
            
            totalCost+=cost
            visited.add(curr)
            
            for nextHouse in range(n):
                if nextHouse not in visited:
                    dist=abs(houses[curr][0]-houses[nextHouse][0])+abs(houses[curr][1]-houses[nextHouse][1])
                    heapq.heappush(minHeap,(dist,nextHouse))
                    
        return totalCost
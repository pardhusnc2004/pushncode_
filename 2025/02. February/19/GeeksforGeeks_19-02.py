'''
    GeeksforGeeks Daily Question (19-02-2025)
    Merge K sorted linked lists
    Python3 solution
'''

class Node:
    def _init_(self,x):
        self.data = x
        self.next = None

import heapq

class Solution:
    def mergeKLists(self, lists):
        # code here
        # return head of merged list
        
        if not lists:
            return None
        heap = []
        for i in lists:
            while i:
                heapq.heappush(heap, i.data)
                i = i.next
        head = Node(-1)
        if not heap:
            return None
        temp = Node(heapq.heappop(heap))
        head.next = temp
        while heap:
            temp.next = Node(heapq.heappop(heap))
            temp = temp.next
        temp.next = None
        return head.next
'''
    GeeksforGeeks Daily Question (20-10-2024)
    Sort a k sorted doubly linked list
    Python3 solution
'''

class DLLNode:
    def __init__(self,val) -> None:
        self.data = val
        self.prev = None
        self.next = None

from heapq import heappush, heappop

class Compare:
    def __init__(self, node):
        self.node = node
    def __lt__(self, other):
        return self.node.data < other.node.data


class Solution:
    def sortAKSortedDLL(self, head, k):
        if head is None:
            return head
        pq = []

        newHead = None
        last = None
        for i in range(k + 1):
            if head is not None:
                heappush(pq, Compare(head))
                head = head.next

        while pq:
            min_node = heappop(pq).node
            if newHead is None:
                newHead = min_node
                newHead.prev = None
                last = newHead
            else:
                last.next = min_node
                min_node.prev = last
                last = min_node
            if head is not None:
                heappush(pq, Compare(head))
                head = head.next
        last.next = None

        return newHead
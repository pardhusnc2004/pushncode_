'''
    GeeksforGeeks Daily Question (25-01-2025)
    Detect Loop in linked list
    Python3 solution
'''

class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None

class Solution:
    def findFirstNode(self, head):
        #code here
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if not fast or not fast.next:
            return Node(-1)
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
        
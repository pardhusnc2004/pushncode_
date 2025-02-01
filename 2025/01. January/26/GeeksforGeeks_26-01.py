'''
    GeeksforGeeks Daily Question (26-01-2025)
    Remove loop in Linked List
    Python3 solution
'''

class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None

class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # code here
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if not fast or not fast.next:
            return
        slow = head
        last = None
        while slow != fast:
            slow = slow.next
            fast = fast.next
        req = slow
        last = slow
        slow = slow.next
        fast = fast.next
        while slow != req:
            last = slow
            slow = slow.next
            fast = fast.next
        last.next = None

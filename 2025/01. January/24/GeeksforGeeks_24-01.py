'''
    GeeksforGeeks Daily Question (24-01-2025)
    Detect Loop in linked list
    Python3 solution
'''

class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None

class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        #code here
        if not head or not head.next:
            return False
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return fast == slow
        
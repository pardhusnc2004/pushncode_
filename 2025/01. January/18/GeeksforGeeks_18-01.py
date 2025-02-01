'''
    GeeksforGeeks Daily Question (18-01-2025)
    Reverse a linked list
    Python3 solution
'''

class Solution:
    def reverseList(self, head):
        # Code here
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev
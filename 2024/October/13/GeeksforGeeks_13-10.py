'''
    GeeksforGeeks Daily Question (13-10-2024)
    Two Smallests in Every Subarray
    Python3 solution
'''

class Node: 
    def __init__(self, data): 
        self.data = data  
        self.next = None

class Solution:
    def deleteAlt(self, head):
        # code here
        if not head or not head.next:
            return head
        while head and head.next:
            head.next = head.next.next
            head = head.next
        return head
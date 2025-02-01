'''
    GeeksforGeeks Daily Question (14-10-2024)
    Count Linked List Nodes
    Python3 solution
'''

class Node: 
    def __init__(self, data): 
        self.data = data  
        self.next = None

class Solution:
    # Function to count nodes of a linked list.
    def getCount(self, head):
        # code here
        res = 0
        while head:
            res += 1
            head = head.next
        return res
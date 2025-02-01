'''
    GeeksforGeeks Daily Question (31-10-2024)
    Insert in Sorted way in a Sorted DLL
    Python3 solution
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Solution:
    #Function to insert a node in a sorted doubly linked list.
    def sortedInsert(self, head, x):
        if head.data >= x:
            newNode = Node(x)
            newNode.next = head
            head.prev = newNode
            head = newNode
            return head
        temp = head
        prev = None
        while temp and temp.data < x:
            prev = temp
            temp = temp.next
        if not temp:
            prev.next = Node(x)
            prev.next.prev = prev
            prev.next.next = None
        else:
            newNode = Node(x)
            newNode.next = temp
            temp.prev = newNode
            prev.next = newNode
        return head
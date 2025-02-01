'''
    GeeksforGeeks Daily Question (23-01-2025)
    Clone List with Next and Random
    Python3 solution
'''

class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None

class Solution:
    def cloneLinkedList(self, head):
        # code here
        nodeMp = {None:None}
        tmp = head
        while tmp:
            if tmp not in nodeMp:
                nodeMp[tmp] = Node(tmp.data)
            tmp = tmp.next
        dummy = Node(-1)
        tail = dummy
        tmp = head
        while tmp:
            node = nodeMp[tmp]
            node.next = nodeMp[tmp.next]
            node.random = nodeMp[tmp.random]
            tail.next = node
            tail = tail.next
            tmp = tmp.next
        return dummy.next

'''
    GeeksforGeeks Daily Question (21-01-2025)
    Linked List Group Reverse
    Python3 solution
'''

class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        # Code here
        res = Node(-1)
        prvGroupLast = res
        
        while head:
            kthNode = self.getKthNode(head, k)
            if not kthNode:
                return res.next
            nxtNode = kthNode.next
            kthNode.next = None
            
            revKthNode = self.reverse(head)
            prvGroupLast.next = revKthNode
            prvGroupLast = head
            head = nxtNode
            
        return res.next
        
    def reverse(self, head):
        tmp = head
        prv = None
        while tmp:
            nxt = tmp.next
            tmp.next = prv
            prv = tmp
            tmp = nxt
        return prv
        
    def getKthNode(self, head, k):
        tmp = head
        last = None
        while k and tmp:
            k -= 1
            last = tmp
            tmp = tmp.next
        return last
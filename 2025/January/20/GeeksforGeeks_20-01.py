'''
    GeeksforGeeks Daily Question (20-01-2025)
    Rotate a Linked List
    Python3 solution
'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    def sortedMerge(self,head1, head2):
        # code here
        res = Node(-1)
        dummy = res
        while head1 and head2:
            if head1.data <= head2.data:
                dummy.next = head1
                head1 = head1.next
            else:
                dummy.next = head2
                head2 = head2.next
            dummy = dummy.next
        while head1:
            dummy.next = head1
            head1 = head1.next
            dummy = dummy.next
        while head2:
            dummy.next = head2
            head2 = head2.next
            dummy = dummy.next
        return res.next
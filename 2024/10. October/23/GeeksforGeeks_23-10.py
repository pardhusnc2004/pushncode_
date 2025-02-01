'''
    GeeksforGeeks Daily Question (23-10-2024)
    Find the Sum of Last N nodes of the Linked List
    Python3 solution
'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        
class Solution:
    def sumOfLastN_Nodes(self, head, n):
        #function should return sum of last n nodes
        def reverse(node):
            temp = node
            prev = None
            while temp:
                next = temp.next
                temp.next = prev
                prev = temp
                temp = next
            return prev
        revHead = reverse(head)
        res = 0
        while n:
            n -= 1
            res += revHead.data
            revHead = revHead.next
        return res
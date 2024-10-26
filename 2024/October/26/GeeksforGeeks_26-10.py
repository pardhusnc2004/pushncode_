'''
    GeeksforGeeks Daily Question (26-10-2024)
    Occurence of an integer in a Linked List
    Python3 solution
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
  
class Solution:
    def count(self, head, key):
        # Code here
        res = 0
        while head:
            if head.data == key:
                res += 1
            head = head.next
        
        return res
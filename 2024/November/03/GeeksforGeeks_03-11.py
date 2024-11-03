'''
    GeeksforGeeks Daily Question (03-11-2024)
    Is Linked List Length Even
    Python3 solution
'''

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = next
        pass

class Solution:
    # your task is to complete this function
    # function should return false if length is even
    # else return true
    def isLengthEven(self, head: Node) -> bool:
        # Code here
        s= 0
        while head:
            s += 1
            head = head.next
        return not s&1
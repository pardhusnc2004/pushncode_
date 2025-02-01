'''
    GeeksforGeeks Daily Question (07-10-2024)
    XOR Linked List
    Python3 solution
'''

class Node:
    def __init__(self, x):
        self.data = x
        self.npx = None

def insert(head, data):
    new_node = Node(data)
    new_node.npx = head
    return new_node

def getList(head):
    result = []
    current = head
    while current is not None:
        result.append(current.data)
        current = current.npx
    return result
'''
    GeeksforGeeks Daily Question (12-11-2024)
    Intersection Point in Y Shaped Linked Lists
    Python3 solution
'''
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = next

def intersetPoint(head1: Node,head2: Node) -> int:
    #code here
    h1, h2 = head1, head2
    while h1 != h2:
        if h1:
            h1 = h1.next
        else:
            h1 = head2
        if h2:
            h2 = h2.next
        else:
            h2 = head1
    
    return h1.data if h1 else -1
'''
    GeeksforGeeks Daily Question (29-10-2024)
    Quick Sort on Linked List
    Python3 solution
'''
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        pass

def quickSort(head):
    #return head after sorting
    
    def sort(h, t):
        if not h or h == t or h.next == t:
            return h
            
        v = h.data
        dummy = Node(0)
        dummy.next = h
        
        prev, w = dummy, h
        
        while w != t:
            nw = w.next
            if w.data < v:
                prev.next = w.next
                w.next = dummy.next
                dummy.next = w
            else:
                prev = prev.next
                
            w = nw
        
        h.next = sort(h.next, t)
        return sort(dummy.next, h)
    return sort(head, None)
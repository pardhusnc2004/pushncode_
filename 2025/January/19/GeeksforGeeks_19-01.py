'''
    GeeksforGeeks Daily Question (19-01-2025)
    Rotate a Linked List
    Python3 solution
'''

class Solution:
    #Function to rotate a linked list.
    def rotate(self, head, k):
        tmp = head
        n = 0
        while tmp:
            n += 1
            tmp = tmp.next
        k %= n
        
        if not k:
            return head
        
        def getList(head, k):
            tmp = head
            for _ in range(k-1):
                tmp = tmp.next
            return tmp
            
        tmp = getList(head, k)
        second = tmp.next
        tmp.next = None
        
        tmp = second
        while tmp and tmp.next:
            tmp = tmp.next
        tmp.next = head
        return second
'''
    GeeksforGeeks Daily Question (17-10-2024)
    Split Linked List Alternatingly
    Python3 solution
'''

class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

class Solution:
    def alternatingSplitList(self, head):
        #Your code here
        f, s = Node(-1), Node(-1)
        ft, st = f, s
        i = 0
        while head:
            if i&1:
                st.next = Node(head.data)
                st = st.next
            else:
                ft.next = Node(head.data)
                ft = ft.next
            head = head.next
            i += 1
        return [f.next, s.next]
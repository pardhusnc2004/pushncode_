'''
    GeeksforGeeks Daily Question (22-01-2025)
    Add Number Linked Lists
    Python3 solution
'''

class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None

class Solution:
    def addTwoLists(self, num1, num2):
        # code here
        rNum1, rNum2 = self.reverseList(num1), self.reverseList(num2)
        res = Node(-1)
        dummy = res
        num1, num2 = rNum1, rNum2
        carry = 0
        while num1 and num2:
            cur = num1.data + num2.data + carry
            carry = cur//10
            cur %= 10
            dummy.next = Node(cur)
            dummy = dummy.next
            num1 = num1.next
            num2 = num2.next
        while num1:
            cur = num1.data + carry
            carry = cur//10
            cur %= 10
            dummy.next = Node(cur)
            dummy = dummy.next
            num1 = num1.next
        while num2:
            cur = num2.data + carry
            carry = cur//10
            cur %= 10
            dummy.next = Node(cur)
            dummy = dummy.next
            num2 = num2.next
        if carry:
            dummy.next = Node(carry)
            dummy = dummy.next
        dummy.next = None
        ret = self.reverseList(res.next)
        while ret and ret.data == 0:
            ret = ret.next
        return ret
        
    def reverseList(self, head):
        tmp = head
        prv = None
        while tmp:
            nxt = tmp.next
            tmp.next = prv
            prv = tmp
            tmp = nxt
        return prv

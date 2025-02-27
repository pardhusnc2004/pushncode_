'''
    GeeksforGeeks Daily Question (27-02-2025)
    Get Min from Stack
    Python3 solution
'''

class Solution:

    def __init__(self):
        # code here
        self.st = []
        
    # Add an element to the top of Stack
    def push(self, x):
        # code here
        if self.st:
            self.st.append([x, min(self.st[-1][-1], x)])
        else:
            self.st.append([x, x])

    # Remove the top element from the Stack
    def pop(self):
        # code here
        if self.st:
            self.st.pop()

    # Returns top element of Stack
    def peek(self):
        # code here
        if self.st:
            return self.st[-1][0]
        return -1

    # Finds minimum element of Stack
    def getMin(self):
        # code here
        if self.st:
            return self.st[-1][-1]
        return -1

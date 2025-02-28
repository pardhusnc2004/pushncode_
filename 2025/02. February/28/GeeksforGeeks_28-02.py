'''
    GeeksforGeeks Daily Question (28-02-2025)
    Evaluation of Postfix Expression
    Python3 solution
'''

class Solution:
    def evaluate(self, arr):
        # code here
        stack = []
        for char in arr:
            if char in "/*+-":
                second = stack.pop()
                first = stack.pop()
                if char == "+":
                    stack.append(first+second)
                elif char == "-":
                    stack.append(first-second)
                elif char == '/':
                    sign = 1 if (first*second) >= 0 else -1
                    stack.append(sign*(abs(first)//abs(second)))
                else:
                    stack.append(first*second)
            else:
                stack.append(int(char))
        return int(stack[-1])
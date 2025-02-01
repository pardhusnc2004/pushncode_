'''
    GeeksforGeeks Daily Question (29-01-2025)
    Implement Pow
    Python3 solution
'''

class Solution:
    def power(self, b: float, e: int) -> float:
        # Code Here
        if e == 0:
            return 1
        if e < 0:
            return self.power(1/b, -e)
        tmp = self.power(b, e//2)
        if e&1:
            return tmp*tmp*b
        else:
            return tmp*tmp
'''
    Leetcode Daily Question (19-10-2024)
    1545. Find Kth Bit in Nth Binary String
    Python3 solution
'''

class Solution:
    def __init__(self):
        self.d = {1: "0"}
        for i in range(2, 21):
            left = self.d[i-1]
            self.d[i] = left+"1"+self.invert(left)
    def invert(self, x):
        res = ""
        for i in x:
            if i == '1':
                res += "0"
            else:
                res += "1"
        return res[::-1]
    def findKthBit(self, n: int, k: int) -> str:
        return self.d[n][k-1]
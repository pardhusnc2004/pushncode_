'''
    GeeksforGeeks Daily Question (30-01-2025)
    N-Queen Problem
    Python3 solution
'''

class Solution:
    def nQueen(self, n):
        # code here
        if n == 1:
            return [[1]]
        if n <= 3:
            return []
        def pos(c, d):
            if c in d:
                return False
            d.reverse()
            # print(d, c)
            for i in range(len(d)):
                if c+i+1 == d[len(d)-i-1]:
                    return False
                if c-i-1 == d[len(d)-i-1]:
                    return False
            return True
        res = []
        def go(row, ds):
            if row == n:
                res.append([i+1 for i in ds[:]])
                return
            for col in range(n):
                if pos(col, ds):
                    go(row+1, ds+[col])
            return
        go(0, [])
        return res
'''
    GeeksforGeeks Daily Question (29-12-2024)
    Intersection of Two arrays with Duplicate Elements
    Python3 solution
'''

class Solution:
    def intersectionWithDuplicates(self, a, b):
        # code here
        res = []
        a, b = set(a), set(b)
        for i in a:
            if i in b:
                res.append(i)
        return res

'''
    GeeksforGeeks Daily Question (28-10-2024)
    Remove duplicates in array
    Python3 solution
'''

class Solution:
    def removeDuplicates(self, arr):
        # code here 
        vis = set()
        res = []
        for i in arr:
            if i not in vis:
                res.append(i)
            vis.add(i)
        return res
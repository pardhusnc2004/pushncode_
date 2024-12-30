'''
    GeeksforGeeks Daily Question (30-12-2024)
    Union of Arrays with Duplicates
    Python3 solution
'''

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def findUnion(self, a, b):
        # code here
        return len(list(set(a).union(set(b))))
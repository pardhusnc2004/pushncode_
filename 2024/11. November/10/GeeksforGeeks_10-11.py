'''
    GeeksforGeeks Daily Question (10-11-2024)
    Union of Two Sorted Arrays with Distinct Elements
    Python3 solution
'''

class Solution:
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        # code here 
        return list(sorted(set(a+b)))

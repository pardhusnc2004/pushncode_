'''
    GeeksforGeeks Daily Question (04-12-2024)
    Strings Rotations of Each Other
    Python3 solution
'''

class Solution:
    
    #Function to check if two strings are rotations of each other or not.
    def areRotations(self,s1,s2):
        #code here
        return len(s1) == len(s2) and s1 in s2+s2
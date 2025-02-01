'''
    GeeksforGeeks Daily Question (01-12-2024)
    Non Repeating Character
    Python3 solution
'''

from collections import Counter
class Solution:
    
    #Function to find the first non-repeating character in a string.
    def nonRepeatingChar(self,S):
        #code here  
        d = Counter(S)
        for i in S:
            if d[i] == 1:
                return i
        return '$'
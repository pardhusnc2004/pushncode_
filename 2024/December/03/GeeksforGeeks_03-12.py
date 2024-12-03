'''
    GeeksforGeeks Daily Question (03-12-2024)
    Min Chars to Add for Palindrome
    Python3 solution
'''

def computeLPSArray(string):

    M = len(string)
    lps = [None] * M
    length = 0
    lps[0] = 0 
    i = 1
    while i < M:
        if string[i] == string[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:

                lps[i] = 0
                i += 1
    return lps


class Solution:

    def minChar(self, string):
        revStr = string[::-1]
        
        concat = string + "$" + revStr
        lps = computeLPSArray(concat)

        return len(string) - lps[-1]
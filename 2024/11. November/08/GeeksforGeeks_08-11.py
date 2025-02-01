'''
    GeeksforGeeks Daily Question (08-11-2024)
    Minimum repeat to make substring
    Python3 solution
'''

class Solution:
    def minRepeats(self, s1, s2):
        # code here
        lps = [0]*len(s2)
        i, j = 1, 0
        while i < len(s2):
            if s2[i] == s2[j]:
                lps[i] = j+1
                i += 1
                j += 1
            else:
                if j:
                    j = lps[j-1]
                else:
                    i += 1
        # print(lps)
        def kmp(string):
            i, j = 0, 0
            while i < len(string) and j < len(s2):
                if string[i] == s2[j]:
                    i += 1
                    j += 1
                if j == len(s2):
                    return True
                elif i < len(string) and string[i] != s2[j]:
                    if j:
                        j = lps[j-1]
                    else:
                        i += 1
            return False
        res = 1
        while not kmp(s1):
            res += 1
            s1 += s1
        return res
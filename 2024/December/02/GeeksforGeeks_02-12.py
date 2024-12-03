'''
    GeeksforGeeks Daily Question (02-12-2024)
    Search Pattern (KMP-Algorithm)
    Python3 solution
'''

class Solution:
    def computeLPSArray(self, pat, M, lps):
        length = 0
        
        lps[0] = 0
        i = 1
        
        while (i < M):
            if pat[i] == pat[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

    def search(self, pat, txt):
        res = []
        M = len(pat)
        N = len(txt)

        lps = [0 for i in range(M + 1)]
        j = 0
        self.computeLPSArray(pat, M, lps)
        
        f = 0
        i = 0
        while i < N:
            if pat[j] == txt[i]:
                j += 1
                i += 1

            if j == M:
                f += 1
                res.append(i - j)
                j = lps[j - 1]

            elif i < N and pat[j] != txt[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i = i + 1

        return res
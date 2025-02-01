'''
    GeeksforGeeks Daily Question (01-01-2025)
    Print Anagrams Together
    Python3 solution
'''

from collections import Counter
class Solution:

    def anagrams(self, arr):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''

        #code here
        d = {}
        for word in arr:
            tmp = str(sorted(word))
            if tmp in d:
                d[tmp].append(word)
            else:
                d[tmp] = [word]
        return list(d.values())

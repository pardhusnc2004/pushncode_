'''
    Leetcode Daily Question (02-11-2024)
    2490. Circular Sentence
    Python3 solution
'''

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        last = sentence[-1][-1]
        for word in sentence.split():
            if word[0] != last:
                return False
            last = word[-1]
        return True

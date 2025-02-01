'''
    Leetcode Daily Question (02-12-2024)
    1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence
    Python3 solution
'''
from typing import List
from collections import *
from bisect import *
from math import *
from heapq import *

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentences = sentence.split()
        n = len(searchWord)
        for i in range(len(sentences)):
            if len(sentences[i]) >= n and sentences[i][0:n] == searchWord:
                return i+1
        return -1
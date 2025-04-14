'''
    GeeksforGeeks Daily Question (14-04-2025)
    Alien Dictionary
    Python3 solution
'''

from collections import defaultdict, deque
from itertools import pairwise

class Solution:
    def findOrder(words):
        adj = defaultdict(set)
        indegree = defaultdict(int)
        for word1, word2 in pairwise(words):
            n = min(len(word1), len(word2))
            i = 0
            while i < n and word1[i] == word2[i]:
                i += 1
            if i < n:
                c1, c2 = word1[i], word2[i]
                if c2 not in adj[c1]:
                    adj[c1].add(c2)
                    indegree[c2] += 1
            elif len(word1) > len(word2):
                return ""
        alphabet = set(c for word in words for c in word)
        q = [c for c in alphabet if indegree[c] == 0]
        order = []
        while q:
            u = q.pop()
            order.append(u)
            for v in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        if any(indegree.values()):
            return ""
        return "".join(order)
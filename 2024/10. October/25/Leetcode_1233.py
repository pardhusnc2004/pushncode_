'''
    Leetcode Daily Question (25-10-2024)
    1233. Remove Sub-Folders from the Filesystem
    Python3 solution
'''
from typing import List

class TrieNode:
    def __init__(self):
        self.links = {}
        self.isEnd = 0

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = TrieNode()
        res = []
        folder.sort()
        for files in folder:
            name = files[1:].split("/")
            dummy = root
            fl = 0
            for subfile in name:
                if subfile not in dummy.links:
                    dummy.links[subfile] = TrieNode()
                    flag = 1
                dummy = dummy.links[subfile]
                if dummy.isEnd:
                    flag = 0
                    break
            dummy.isEnd = 1
            if flag:
                res.append(files)
        return res
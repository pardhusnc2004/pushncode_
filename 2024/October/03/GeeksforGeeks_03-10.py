'''
    GeeksforGeeks Daily Question (03-10-2024)
    Majority Vote
    Python3 solution
'''

class Solution:
    def findMajority(self, nums):
        e1, e2, c1, c2 = -1e9, -1e9, 0, 0
        for i in nums:
            if i == e1:
                c1+=1
            elif i == e2:
                c2+=1
            elif c1 == 0:
                e1, c1 = i, 1
            elif c2 == 0:
                e2, c2 = i, 1
            else:
                c1-=1
                c2-=1
        c1, c2 = 0, 0
        for i in nums:
            if i==e1: c1+=1
            elif i==e2: c2+=1
        ret = []
        if c1>len(nums)//3: ret.append(e1)
        if c2>len(nums)//3: ret.append(e2)
        return ret if ret else [-1]
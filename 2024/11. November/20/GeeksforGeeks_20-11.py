'''
    GeeksforGeeks Daily Question (20-11-2024)
    Majority Element II
    Python3 solution
'''

class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, nums):
        #Your Code goes here.
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
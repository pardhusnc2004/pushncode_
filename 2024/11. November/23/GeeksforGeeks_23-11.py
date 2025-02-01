'''
    GeeksforGeeks Daily Question (23-11-2024)
    Minimize the Heights I
    Python3 solution
'''

class Solution:
    def getMinDiff(self,k, nums):
        # code here
        N = len(nums)
        nums.sort()
        res = nums[-1]-nums[0]
        for i in range(N-1):
            maxi, mini = max(nums[i]+k, nums[-1]-k), min(nums[0]+k, nums[i+1]-k)
            res = min(res, maxi-mini)
        return res

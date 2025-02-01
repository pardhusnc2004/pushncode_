'''
    GeeksforGeeks Daily Question (28-12-2024)
    Find All Triplets with Zero Sum
    Python3 solution
'''

class Solution:
    def findTriplets(self, nums):
        # Your code here
        res = []
        n = len(nums)
        for i in range(n-1):
            d = {}
            target = -nums[i]
            for j in range(i+1, n):
                if (target - nums[j]) in d:
                    for k in d[(target - nums[j])]:
                        res.append([i, k, j])
                if nums[j] in d:
                    d[nums[j]].append(j)
                else:
                    d[nums[j]] = [j]
            d.clear()
        return res
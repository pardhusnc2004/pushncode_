'''
    Leetcode Daily Question (03-10-2024)
    1590. Make Sum Divisible by P
    Python3 solution
'''

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)

        d = {0:-1}
        cursum = 0

        sum_ = sum(nums)
        if not sum_%p:
            return 0

        res = 1e9
        req = sum_%p

        for i in range(n):
            cursum += nums[i]
            cursum %= p
            if (cursum-req+p)%p in d:
                res = min(res, i-d[(cursum-req+p)%p])
            d[cursum] = i

        return res if res != n else -1
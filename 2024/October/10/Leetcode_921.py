'''
    Leetcode Daily Question (10-10-2024)
    962. Maximum Width Ramp
    Python3 solution
'''

from typing import List

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        st = []
        n = len(nums)
        def helper(idx, arr):
            num = nums[idx]
            i, j = 0, len(arr)-1
            if nums[arr[0]] <= num:
                return idx-arr[0]
            maxPoss = idx
            while i <= j:
                mid = (i+j)>>1
                check = nums[arr[mid]]
                if num >= check:
                    maxPoss = arr[mid]
                    j = mid-1
                else:
                    i = mid+1
            return idx-maxPoss
        res = 0
        for i in range(n):
            if not st or nums[st[-1]] > nums[i]:
                st.append(i)
            else:
                temp = helper(i, st)
                # print(i, temp, st)
                res = max(res, temp)
        return res
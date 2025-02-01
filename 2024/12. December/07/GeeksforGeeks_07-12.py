'''
    GeeksforGeeks Daily Question (07-12-2024)
    Count Inversions
    Python3 solution
'''

class Solution:
    #User function Template for python3
    def inversionCount(self, nums):
        # Your Code Here
        n = len(nums)
        def merge(left, mid, right):
            new_arr = []
            res = 0
            i, j = left, mid+1
            while i <= mid and j <= right:
                if nums[i] > nums[j]:
                    res += mid-i+1
                    j += 1
                else:
                    i += 1
            i, j = left, mid+1
            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    new_arr.append(nums[i])
                    i += 1
                else:
                    new_arr.append(nums[j])
                    j += 1
            while i <= mid:
                new_arr.append(nums[i])
                i += 1
            while j <= right:
                new_arr.append(nums[j])
                j += 1
            for k in range(left, right+1):
                nums[k] = new_arr[k-left]
            return res
        def ms(left, right):
            if left >= right:
                return 0
            mid = (left+right)//2
            left_res = ms(left, mid)
            right_res = ms(mid+1, right)
            return left_res + right_res + merge(left, mid, right)
        return ms(0, len(nums)-1)

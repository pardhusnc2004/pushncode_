'''
    GeeksforGeeks Daily Question (06-01-2025)
    Sum Pair closest to target
    Python3 solution
'''

class Solution:
    def sumClosest(self, arr, target):
        # code here
        arr.sort() 
        left = 0
        right = len(arr)-1
        closest_sum = float('inf')
        closest_pair = []
        
        while left < right:
            current_sum = arr[left] + arr[right]
            
            if abs(target - current_sum) < abs(target - closest_sum):
                closest_sum = current_sum
                closest_pair = [arr[left],arr[right]]
                
            if current_sum < target:
                left += 1
                
            elif current_sum > target:
                right -= 1
                
            else:
                break
            
        return closest_pair
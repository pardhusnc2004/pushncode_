'''
    GeeksforGeeks Daily Question (21-10-2024)
    Split the Array
    Python3 solution
'''

class Solution:
    def countgroup(self,arr):
        ans=0
        for i in arr:
            ans^=i
        if ans==0:
            for i in range(len(arr)-1):
                if len(arr)%2==0:
                    return pow(2,len(arr)-1)-1
                return len(arr)
        return 0
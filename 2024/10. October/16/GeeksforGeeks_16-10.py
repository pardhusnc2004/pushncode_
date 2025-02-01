'''
    GeeksforGeeks Daily Question (16-10-2024)
    Two Swaps
    Python3 solution
'''

class Solution:
    def checkSorted(self, arr):
        #code here
        c = 0
        n = len(arr)
        a = sorted(arr)
        for i in range(n):
            j = i+1
            f = 1
            while arr[j-1]!=i+1:
                j = arr[j-1]
                if f:
                    f=0
                    c+=1
                
            arr[i], arr[j-1] = arr[j-1], arr[i]
            
            if arr==a or c>2:
                break
        return c==0 or c==2
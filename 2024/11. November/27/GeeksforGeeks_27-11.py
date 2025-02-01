'''
    GeeksforGeeks Daily Question (27-11-2024)
    Smallest Positive Missing Number
    Python3 solution
'''

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        #Your code here
        pos = [0]
        arr = list(set(arr))
        arr.sort()
        for i in arr:
            if i > 0:
                if i != pos[-1]+1:
                    return pos[-1]+1
                pos.append(i)
        return pos[-1]+1
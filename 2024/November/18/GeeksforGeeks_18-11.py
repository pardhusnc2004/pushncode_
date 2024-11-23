'''
    GeeksforGeeks Daily Question (18-11-2024)
    Rotate Array
    Python3 solution
'''

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        #Your code here
        n = len(arr)
        d %= n
        def reverse(i, j):
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        reverse(0, d-1)
        reverse(d, n-1)
        reverse(0, n-1)
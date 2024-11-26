'''
    GeeksforGeeks Daily Question (26-11-2024)
    Max Circular Subarray Sum
    Python3 solution
'''

from math import inf
#Complete this function
#Function to find maximum circular subarray sum.
def circularSubarraySum(arr):
    n = len(arr)
    count = 0
    maxx = -inf
    for i in range(0, n):
        if (arr[i] > maxx):
            maxx = arr[i]
        if (arr[i] < 0):
            count = count + 1

    if (count == n):
        return maxx

    max_kadane = kadane(arr)

    max_wrap = 0
    for i in range(0, n):
        max_wrap += arr[i]
        arr[i] = -arr[i]


    max_wrap = max_wrap + kadane(arr)

    if max_wrap > max_kadane:
        return max_wrap
    else:
        return max_kadane
        
def kadane(arr):

    max_so_far = 0
    max_ending_here = 0
    n = len(arr)
    for i in range(0, n):
        max_ending_here = max_ending_here + arr[i]

        if (max_ending_here < 0):
            max_ending_here = 0

        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
    return max_so_far


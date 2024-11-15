'''
    GeeksforGeeks Daily Question (15-11-2024)
    Second Largest
    Python3 solution
'''

class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        m1, m2 = -1, -1
        for i in arr:
            if i > m1:
                m2 = m1
                m1 = i
            else:
                if i != m1:
                    m2 = max(m2, i)
        return m2
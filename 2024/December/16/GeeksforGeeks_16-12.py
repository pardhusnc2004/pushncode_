'''
    GeeksforGeeks Daily Question (16-12-2024)
    K-th element of two Arrays
    Python3 solution
'''

class Solution:
    def kthElement(self, a, b, k):
        i, j = 0, 0
        n1, n2 = len(a), len(b)
        for _ in range(k-1):
            if(i < n1 and j < n2):
                if(a[i] <= b[j]):
                    i += 1
                else:
                    j += 1
            elif i < n1:
                i += 1
            else:
                j += 1
        if i < n1 and j < n2:
            return min(a[i], b[j])
        if i < n1:
            return a[i]
        return b[j]
        pass

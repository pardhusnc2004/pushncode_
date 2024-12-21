'''
    GeeksforGeeks Daily Question (21-12-2024)
    Rotate by 90 degree
    Python3 solution
'''

class Solution:
    
    #Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(self, mat): 
        # code here
        n = len(mat)
        def reve(i):
            l, r = 0, n-1
            while l < r:
                i[l], i[r] = i[r], i[l]
                l += 1
                r -= 1
        for i in mat:
            reve(i)
        for i in range(n):
            for j in range(i+1, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

        return mat
'''
    GeeksforGeeks Daily Question (05-11-2024)
    Rotate by 90 degree
    Python3 solution
'''

def rotate(matrix): 
    #code here
    m = len(matrix)
    for i in range(m):
        for j in range(i+1, m):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    def reverse(ls):
        i, j = 0, m-1
        while i < j:
            ls[i], ls[j] = ls[j], ls[i]
            i += 1
            j -= 1
    for ls in matrix:
        reverse(ls)
    return matrix
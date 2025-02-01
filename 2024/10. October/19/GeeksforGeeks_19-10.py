'''
    GeeksforGeeks Daily Question (19-10-2024)
    Nearest multiple of 10
    Python3 solution
'''

class Solution:
    def roundToNearest (self, s) : 
        if len(s) < 2:
            if int(s) <= 5:
                return "0"
            else:
                return "10"
        if int(s[-1]) <= 5:
            return s[:-1]+"0"
        else:
            ns = "0"
            carry = 1
            for i in range(len(s)-2, -1, -1):
                temp = int(s[i])+carry
                ns += str(temp%10)
                carry = temp//10
            return ns[::-1]
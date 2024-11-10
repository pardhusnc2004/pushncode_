'''
    GeeksforGeeks Daily Question (09-11-2024)
    Minimum sum
    Python3 solution
'''

class Solution:
    def minSum(self, arr):
        # code here
        n = len(arr)
        if 0 == n:
            return 0
        if 1 == n:
            return arr[0]
        freq = [0] * 10
        for digit in arr:
            if digit:
                freq[digit] += 1
        s = []
        remainder = 0
        odd = False
        for digit in range(9, 0, -1):
            count = freq[digit]
            if count:
                if odd:
                    remainder += digit
                    count -= 1
                    s.append(str(remainder % 10))
                    remainder //= 10
                    odd = False
                for _ in range(count // 2):
                    remainder += digit * 2
                    s.append(str(remainder % 10))
                    remainder //= 10
                if count % 2:
                    odd = True
                    remainder += digit
        if remainder:
            s.append(str(remainder))
        s.reverse()
        return ''.join(s)

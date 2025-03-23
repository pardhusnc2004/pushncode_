'''
    GeeksforGeeks Daily Question (23-03-2025)
    Total Decoding Messages
    Python3 solution
'''

class Solution:
	def countWays(self, digits):
		# Code here
            n = len(digits)
            dp = [0]*(n+1)
            dp[-1] = 1
            for i in range(n-1, -1, -1):
                if digits[i] == '0':
                    continue
                dp[i] += dp[i+1]
                if 10 <= int(digits[i:i+2]) <= 26:
                    dp[i] += dp[i+2]
            # print(dp[0])
            return dp[0]
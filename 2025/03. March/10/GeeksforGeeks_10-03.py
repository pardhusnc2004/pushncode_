'''
    GeeksforGeeks Daily Question (10-03-2025)
    Edit Distance
    Python3 solution
'''

class Solution:
	def editDistance(self, s1, s2):
		# Code here
          
            n1, n2 = len(s1), len(s2)
            dp = [[n1+n2+1]*(n2+1) for _ in range(n1+1)]
            dp[0][0] = 0
            for i in range(1, n1+1):
                dp[i][0] = i
            for j in range(1, n2+1):
                dp[0][j] = j
            for i in range(1, n1+1):
                for j in range(1, n2+1):
                    if s1[i-1] == s2[j-1]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = 1+min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
            return dp[-1][-1]
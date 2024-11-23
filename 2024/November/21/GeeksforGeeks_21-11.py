'''
    GeeksforGeeks Daily Question (21-11-2024)
    Stock Buy and Sell – Multiple Transaction Allowed
    Python3 solution
'''

class Solution:
    def maximumProfit(self, prices) -> int:
        last_bought = 0
        total_earned = 0
        for i in range(len(prices) -1):
            if prices[i] < prices[i+1] and last_bought == 0:
                last_bought = prices[i]
                if prices[i]==0:
                    last_bought = .0001
            if prices[i] > prices[i+1]:  
                if last_bought != 0:
                    total_earned += prices[i] - int(last_bought)
                    last_bought = 0
        if last_bought != 0:
            total_earned += prices[-1] - int(last_bought)
            last_bought = 0   
        
        return total_earned
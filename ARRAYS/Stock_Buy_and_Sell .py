class Solution:
    def maxProfit(self, s):
        bestBuy = s[0]
        maxProfit = 0

        for i in range(len(s)):
            maxProfit = max(maxProfit, s[i] - bestBuy)
            bestBuy = min(bestBuy, s[i])

        return maxProfit

# Example usage:
print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))

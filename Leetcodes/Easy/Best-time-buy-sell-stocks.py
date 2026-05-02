# Best Time to Buy and Sell Stock
# Given an array prices where prices[i] is the price on day i, choose one buy day and one later sell day to maximize profit.
# Return max profit, or 0 if no profit is possible.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy at 1, sell at 6 → profit 5.

# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0


def maxProfit(prices):
    min_price = float("inf")
    best = 0
    for price in prices:
        best = max(best, price - min_price)
        min_price = min(min_price, price)
    return best


print(maxProfit([7, 1, 5, 3, 6, 4]))  # 5
print(maxProfit([7, 6, 4, 3, 1]))  # 0

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def maxProfit(prices):
    buy = 0
    sell = 1
    max_profit = 0
    while sell < len(prices):
        if prices[sell] > prices[buy]:
            profit = prices[sell] - prices[buy]
            max_profit = max(profit, max_profit)
        else:
            buy = sell
        sell = sell + 1
    return max_profit

prices = [7,6,4,3,1]
print(maxProfit(prices))
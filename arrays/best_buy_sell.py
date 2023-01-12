# update 2 pointers to find max difference from right to left
def maxProfit(prices) -> int:
    n = len(prices)
    buy = 0
    sell = buy + 1
    m = 0
    while sell < n:
        if prices[sell] < prices[buy]:
            buy = sell
            sell = buy + 1
        else:
            sub = prices[sell] - prices[buy]
            if sub > m:
                m = sub
            sell += 1
    return m

prices = [7,6,5,4,3,2,1,8]
print(maxProfit(prices))






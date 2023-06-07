def maximumProfit(prices):
    m = prices[0]
    cost = 0
    for i in range(1,len(prices)):
        c = prices[i]-m
        if c>cost:
           cost = c
        if m>prices[i]:
            m = prices[i]
    return cost
print(maximumProfit([98, 101, 66, 72]))

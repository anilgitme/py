class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return prices
        profit = 0
        curMin = prices[0]
        for i in range(1,len(prices)):
            if prices[i] <= curMin:
                curMin = prices[i]
            else:
                profit += prices[i] - curMin
                curMin = prices[i]
        return profit

A = Solution()
print(A.maxProfit([9,3,7,1,10,8]))
print(A.maxProfit([9]))
print(A.maxProfit([]))
print(A.maxProfit([7,6,4,3,1]))
print(A.maxProfit([7,1,5,3,6,4]))
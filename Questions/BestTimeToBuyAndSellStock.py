class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = float("inf")
        profit = 0

        for i, price in enumerate(prices):
            if buyPrice > price:
                buyPrice = price
            else:
                profit = max(profit, price - buyPrice)

        return profit
    
    # Attempt 2
    
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         buy, sell, min_index, ans = 0, 1, 0, 0
        
#         while ( sell < len(prices) ):
#             if (prices[buy] > prices[min_index]):
#                 buy = min_index
            
#             ans = max(ans, prices[sell] - prices[buy])
            
#             if (prices[sell] < prices[min_index]):
#                 min_index = sell
#             sell += 1
        
#         if ans:
#             return ans
#         return 0

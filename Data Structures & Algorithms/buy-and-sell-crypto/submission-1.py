# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         ans = 0
#         L = 0

#         for i in range(len(prices)):
#             for j in range(i+1, len(prices)):
#                 ans = max(ans, prices[j] - prices[i])    

#         return ans    

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        ans = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                ans = max(profit, ans)
            else:
                l = r
            r+=1
        return ans
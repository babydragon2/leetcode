from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 10**4+1
        max_profit = 0

        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i]-min_price)

        return max_profit



s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([7,6,4,3,1]))




        

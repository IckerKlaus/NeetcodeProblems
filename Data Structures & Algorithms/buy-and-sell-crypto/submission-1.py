class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Time: O(n)
        Space: O(1)
        """
        max_profit = 0
        l= 0
        for r in range(1, len(prices)):
            if prices[l] < prices[r]:
                max_profit = max(max_profit, prices[r] - prices[l])
            else:
                l = r
        return max_profit
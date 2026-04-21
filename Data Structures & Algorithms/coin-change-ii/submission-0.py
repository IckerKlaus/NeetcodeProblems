class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        Dynamic Programming Bottom Up
        Pseudo code:
        dp arr of 0 of lenght amount
        dp of 0 is 1
        iterate in reverse order through my coins
            iterate through 1 until amount + 1
                dp of amount += dp of amount - current coin if current coin <= amount else dp of amount = 0
        return dp of amount

        Time: O(c * a)
        Space: O(a)
        """
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins) - 1, -1, -1):
            for a in range(1, amount + 1):
                dp[a] += dp[a - coins[i]] if coins[i] <= a else 0
        return dp[amount]
            
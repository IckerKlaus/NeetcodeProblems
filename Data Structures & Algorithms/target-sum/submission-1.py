class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        Dynamic Programming Bottom Up
        Time: O(n * sum(nums))
        Space: O(sum(nums))
        """
        dp = defaultdict(int) # pos_sum -> ways to pos_sum
        dp[0] = 1 # one way to reach sum 0 before using any numbers
        for num in nums:
            temp = defaultdict(int)
            for total, count in dp.items():
                temp[total + num] += count
                temp[total - num] += count
            dp = temp
        return dp[target]
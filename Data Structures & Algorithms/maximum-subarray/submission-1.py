class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Time: O(n)
        Space: O(1)
        """
        maxSum = nums[0]
        curSum = 0
        for n in nums:
            curSum = max(curSum, 0)
            curSum += n
            maxSum = max(maxSum, curSum)
        return maxSum
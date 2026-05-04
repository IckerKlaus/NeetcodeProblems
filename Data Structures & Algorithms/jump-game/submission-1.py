class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Greedy
        O(n)
        O(1)
        """
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        return True if goal == 0 else False
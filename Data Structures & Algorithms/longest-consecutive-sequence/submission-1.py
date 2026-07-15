class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Time: O(n)
        Space: O(n)
        """
        longest = 0
        numset = set(nums)
        l = 0
        for num in numset:
            if (num - 1) not in numset:
                curlongest = 1
                while (num + curlongest) in numset:
                    curlongest += 1
                longest = max(longest, curlongest)
        return longest
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Time: O(n)
        Space: O(n)
        
        declare hashmap key=val -> val of nums = idx of nums
        iterate through nums:
            substraction = target - curnum
            if substraction in hashmap:
                return index substraction and curnum
            add curnum and idx to hashmap
        """
        values = defaultdict(int)
        for i in range(len(nums)):
            substraction = target - nums[i]
            if substraction in values:
                return [values[substraction], i]
            values[nums[i]] = i
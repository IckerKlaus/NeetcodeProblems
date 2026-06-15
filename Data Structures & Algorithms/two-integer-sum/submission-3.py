class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        5
        1   2   3   4
                i
        diff = 2
        hashmap = 1:0, 2:1,  #num:idx
        return [i, hashmap[diff]]
        """
        hashmap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[nums[i]] = i
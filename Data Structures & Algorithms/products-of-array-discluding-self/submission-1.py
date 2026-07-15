class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Time: O(n)
        Space: O(n)
        The idea is use Prefix and Suffix
        Because we want all of the products
        of the adjacent values
        Pseudocode:
        declare prefix array of [1] of len nums
        declare suffix array of [1] of len nums

        traverse nums starting at idx 1 until len of nums - 1
            prefix o idx = prefix of idx - 1 * nums of idx -1
        
        traverse nums starting at idx len of nums -2 until idx 0
            suffix of idx = suffix of idx + 1 * nums of idx + 1
        
        declare result array [prefix[idx] * suffix[idx]]
        resturr result array
        """

        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        
        answer = [prefix[i] * suffix[i] for i in range(len(nums))]

        return answer
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Time: O(n)
        Space: O(n)
        1   2   2   3   4   5
                i
        set =   1   2
        return True
        """
        unic = set()
        for n in nums:
            if n in unic:
                return True
            unic.add(n)
        return False
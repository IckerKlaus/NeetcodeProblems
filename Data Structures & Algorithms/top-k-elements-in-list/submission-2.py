class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Bucket Sort
        Time: O(n)
        Space: O(n)
        Idea: Use the logic of bucketsort, use the idx of bucket
        arr to save the val that have this amount in nums, then
        iterate in reverse through my bucket arr until k <= 0.
        """
        bucket = [[] for i in range(len(nums) + 1)]
        count = {}
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for i, v in count.items():
            bucket[v].append(i)
        
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res






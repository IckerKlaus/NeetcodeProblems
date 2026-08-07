class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Time: O(n)
        Space: O(n)
        """
        stack = [] # (idx, height)
        max_area = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, hei = stack.pop()
                cur_area = hei * (i - idx)
                max_area = max(max_area, cur_area)
                start = idx
            stack.append((start, h))
        
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        
        return max_area
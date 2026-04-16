class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        2D Dynamic Programming
        Time: O(n + m)
        Space: O(n)
        """
        row = [1] * n
        for i in range(m - 1):
            tempRow = [1] * n
            for j in range(n -2, -1, -1):
                tempRow[j] = tempRow[j + 1] + row[j]
            row = tempRow
        return row[0]
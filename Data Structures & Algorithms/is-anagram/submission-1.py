class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Time: O(n)
        Space: O(n)
        c   a   t
                    i

        t   c   a
                    j

        word1set = c:1, a:1, t:1
        word2set = t:1, c:1, a:1

        return word1set == word2set
        """
        if len(s) != len(t):
            return False

        word1 = {}
        word2 = {}
        for c in s:
            word1[c] = 1 + word1.get(c, 0)
        
        for c in t:
            word2[c] = 1 + word2.get(c, 0)
        
        return word1 == word2

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Time: O(n)
        Space: O(n)
        """
        if len(s) != len(t):
            return False
        
        s1 = defaultdict(int)
        s2 = defaultdict(int)
        for i in range(len(s)):
            s1[s[i]] = 1 + s1.get(s[i], 0)
            s2[t[i]] = 1 + s2.get(t[i], 0)
        
        return s1 == s2
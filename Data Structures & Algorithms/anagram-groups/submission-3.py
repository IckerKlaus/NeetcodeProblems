class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Time: O(n * m)
        Space: O(n * m)
        hashmap = key:val -> arrASCII:[word1, ...]
        iterate through strs
            convert str in arr ascii
            hashmap[tuple(arrASCII)].append(str)
        return list(hashmap.values())
        """
        hashmap = defaultdict(list)
        for s in strs:
            arrASCII = [0] * 26
            for c in s:
                arrASCII[ord(c) - ord('a')] += 1
            hashmap[tuple(arrASCII)].append(s)
        return list(hashmap.values())
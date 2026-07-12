class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Time: O(n * m)
        Space: O(n * m)
        declare hashmap key=val -> ASCII of the hole str = list(str)
        iterate through strs:
            declare array of 0 of length 26
            iterate through curstr:
                translate curchar int ASCII and map it in my array and add 1 to this idx
            identify the array in hashmap and append str
        return all of the values of my hashmap and translate into a list of list
        """
        hashmap = defaultdict(list)
        for s in strs:
            asciistr = [0] * 26
            for c in s:
                asciistr[ord(c) - ord('a')] += 1
            hashmap[tuple(asciistr)].append(s)
        return list(hashmap.values())
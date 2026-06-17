class Solution:
    """
    Idea:
    encode: w is a string and I would add first the len of each
    str in strs separate by ",". Then I would add an "#" to separate
    the len from the words and then I would add all of the str in
    strs.
    
    decode: I would iterate through s and append every len until #,
    then slice every str in s using their sizes.
    """
    def encode(self, strs: List[str]) -> str:
        """
        Where m is the sum of lengths of all the strings and n is the number of
        strings.
        Time: O(n + m)
        Space: O(n + m)
        """
        if not strs:
            return ""
        
        w = ""
        sizes = []
        
        for s in strs:
            sizes.append(len(s))
        for size in sizes:
            w += str(size)
            w += ","
        
        w += "#"

        for s in strs:
            w += s
        
        return w

    def decode(self, s: str) -> List[str]:
        """
        Where m is the sum of lengths of all the strings and n is the number of
        strings.
        Time: O(n + m)
        Space: O(n + m)
        """
        if s == "":
            return []
        
        sizes = []
        i = 0

        while s[i] != "#":
            num = ""
            while s[i] != ",":
                num += s[i]
                i += 1
            i += 1
            sizes.append(int(num))
        
        i += 1

        res = []
        for sz in sizes:
            res.append(s[i: i + sz])
            i += sz
        
        return res





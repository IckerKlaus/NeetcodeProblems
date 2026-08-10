class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """
        Time: O(n * m)
        Space: O(n * m)
        """
        res = []
        line, length = [], 0
        i = 0

        while i < len(words):
            if length + len(line) + len(words[i]) <= maxWidth:
                line.append(words[i])
                length += len(words[i])
                i += 1
            else:
                extra_space = maxWidth - length
                space = extra_space // max(1, (len(line) - 1))
                reminder = extra_space % max(1, (len(line) - 1))
                
                for j in range(max(1, (len(line) - 1))):
                    line[j] += " " * space
                    if reminder:
                        line[j] += " "
                        reminder -= 1
                
                res.append("".join(line))
                line, length = [], 0
        
        last_line = " ".join(line)
        trail_space = maxWidth - len(last_line)
        res.append(last_line + " " * trail_space)
        
        return res
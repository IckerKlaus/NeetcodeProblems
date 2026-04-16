class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        """
        Topological Sort (Directed Acyclic Graph)
        Time: O(C)
        Space: O(E + V)
        a - z
        w -> e -> r -> t -> f valid
        z <-> x invalid because its a cycle
        """
        adj = {c:set() for word in words for c in word}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            # apple, app -> not sorted lexicographically because the second one is a prefix
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]: return ""
            # frid, friend
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        # Help to know if there is a cycle in the graph
        visited = {} # c: False (visited, not in path), c: True (visited, in path)
        res = []
        # Traversing the graph in postorder: Final character -> First character (lexicographically 
        # decreasing order)
        def dfs(c):
            if c in visited: return visited[c]
            visited[c] = True
            for nei in adj[c]:
                if dfs(nei): return True
            visited[c] = False
            res.append(c)
        for c in adj:
            if dfs(c): return ""
        res.reverse() # reverse the list so it would be in lexicographically increasing order
        return "".join(res)
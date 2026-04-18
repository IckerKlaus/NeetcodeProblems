class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        m = edges
        Time: O(m) thanks to the point 1 and 2 (both generate the ackerman inverse function that is aproximetly O(1) in time complexity)
        Space: O(m)
        """
        par = {}
        rank = {}

        for i in range(1, len(edges) + 1):
            par[i] = i
            rank[i] = 0

        def find(n):
            p = par[n]
            while p != par[p]:
                # 1. path comprehesion for max height of 1
                par[p] = par[par[p]] 
                p = par[p]
            return p
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2: return False
            
            # 2. select parent by rank (height) make a balanced tree
            if rank[p1] > rank[p2]:
                par[p2] = p1
            elif rank[p2] > rank[p1]:
                par[p1] = p2
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2): return [n1, n2]
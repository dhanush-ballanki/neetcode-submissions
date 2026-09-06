from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        adj = defaultdict(list)
        for src, dst in tickets:
            adj[src].append(dst)
            
        for src in adj:
            adj[src].sort(reverse=True)
            
        res = []
    
        def dfs(airport):
            while adj[airport]:
                next_dest = adj[airport].pop()
                dfs(next_dest)
            res.append(airport)
            
        dfs("JFK")
        
        return res[::-1]
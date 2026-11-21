class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)
            
        new_parent = list(parent)
        last_seen = {}
        
        def dfs(u: int):
            char = s[u]
            prev = last_seen.get(char)
            if prev is not None:
                new_parent[u] = prev
            
            last_seen[char] = u
            for v in adj[u]:
                dfs(v)
                
            if prev is None:
                del last_seen[char]
            else:
                last_seen[char] = prev
                
        dfs(0)
        
        new_adj = [[] for _ in range(n)]
        for i in range(1, n):
            new_adj[new_parent[i]].append(i)
            
        ans = [1] * n
        
        def calc_size(u: int) -> int:
            for v in new_adj[u]:
                ans[u] += calc_size(v)
            return ans[u]
            
        calc_size(0)
        return ans
class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        import sys
        sys.setrecursionlimit(200000)

        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        parent = [0] * n
        depth = [0] * n
        heavy = [-1] * n
        head = [0] * n
        pos = [0] * n
        tree_size = [0] * n
        cur_pos = 0

        def dfs_size(u, p, d):
            parent[u] = p
            depth[u] = d
            size = 1
            max_c_size = 0
            for v in g[u]:
                if v != p:
                    c_size = dfs_size(v, u, d + 1)
                    size += c_size
                    if c_size > max_c_size:
                        max_c_size = c_size
                        heavy[u] = v
            tree_size[u] = size
            return size

        def dfs_hld(u, h):
            nonlocal cur_pos
            head[u] = h
            pos[u] = cur_pos
            cur_pos += 1

            if heavy[u] != -1:
                dfs_hld(heavy[u], h)

            for v in g[u]:
                if v != parent[u] and v != heavy[u]:
                    dfs_hld(v, v)

        dfs_size(0, -1, 0)
        dfs_hld(0, 0)

        bit = [0] * (n + 1)

        def update_bit(idx, val):
            idx += 1
            while idx <= n:
                bit[idx] ^= val
                idx += idx & -idx

        def query_bit(idx):
            res = 0
            idx += 1
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & -idx
            return res

        def query_range(l, r):
            if l > r:
                l, r = r, l
            return query_bit(r) ^ query_bit(l - 1)

        vals = [1 << (ord(ch) - ord('a')) for ch in s]
        for i in range(n):
            update_bit(pos[i], vals[i])

        def path_query(u, v):
            res_mask = 0
            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u
                res_mask ^= query_range(pos[head[u]], pos[u])
                u = parent[head[u]]

            if depth[u] > depth[v]:
                u, v = v, u
            res_mask ^= query_range(pos[u], pos[v])
            return res_mask

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                new_val = 1 << (ord(c) - ord('a'))
                update_bit(pos[u], vals[u] ^ new_val)
                vals[u] = new_val
            else:
                u, v = int(parts[1]), int(parts[2])
                mask = path_query(u, v)
                ans.append((mask & (mask - 1)) == 0)

        return ans
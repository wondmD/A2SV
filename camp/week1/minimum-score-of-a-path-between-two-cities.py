class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent = [i for i in range(n+1)]
        size = [1] * (n+1)
        def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y, dist):
            nonlocal short
            parent_x = find(x)
            parent_y = find(y)
            short = min(short, dist)
            if parent_x != parent_y:
                if size[parent_x] > size[parent_y]:
                    parent[parent_y] = parent_x
                    size[parent_x] += size[parent_y]
                else:
                    parent[parent_x] = parent_y
                    size[parent_y] += size[parent_x]
        short = float('inf')
        for start, end, dist in roads:
            union(start, end, dist)
        ans = float('inf')
        for start, end, dist in roads:
            if parent[start] == parent[1] or parent[end] == parent[1]:
                ans = min(ans, dist)
        if parent[1] == parent[n]:
            return ans
        else:
            return  short


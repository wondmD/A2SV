class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = [defaultdict(set), defaultdict(set)]
        ans = [-1] * n
        vis = set()
        for node_1, node_2 in redEdges:
            graph[0][node_1].add(node_2)
        for node_1, node_2 in blueEdges:
            graph[1][node_1].add(node_2)
        q = deque([(0, 0, 0)])
        while q:
            node, color, step = q.popleft()
            if (ans[node] == -1) or (ans[node] > step):
                ans[node] = step
                
            vis.add((node, color))
            next_color = (color + 1) % 2
            for nn in graph[next_color][node]:
                if (nn, next_color) not in vis:
                    q.append((nn, next_color, step + 1))
            
        vis = set()
        q = collections.deque([(0, 1, 0)])
        while q:
            node, color, step = q.popleft()
            if (ans[node] == -1) or (ans[node] > step):
                ans[node] = step
                
            vis.add((node, color))
            next_color = (color + 1) % 2
            for nn in graph[next_color][node]:
                if (nn, next_color) not in vis:
                    q.append((nn, next_color, step + 1))
        return ans
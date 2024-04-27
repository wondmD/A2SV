from sys import stdin
from collections import defaultdict, deque
# from bisect import bisect_left, bisect_right

def sol():
    n, m= map(int, stdin.readline().split())
    a, b= map(int, stdin.readline().split())
    graph = defaultdict(list)

    for i in range(m):
        v1, v2= map(int, stdin.readline().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    q = deque([a])
    v = set([a])
    path = []
    while q:
        n = len(q)
        for i in range(n):
            node = q.popleft()
            v.add(node)
            if sum(graph[node]):
                path.append(node)
            if node == b:
                return path
            for i in range(len(graph[node])):
                nodes = graph[node][i]
                if nodes not in v:
                    q.append(nodes)

                if nodes == b:
                    path.append(b)
                    return path
                
    return -1

print(sol())
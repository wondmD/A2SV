from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

def sol():
    # pass
    n , m= map(int, stdin.readline().split())
    graph = defaultdict(list)
    for _ in range(m):
        a, b= map(int, stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    cycles = []
    visited = set()
    for v in graph:
        if v not in visited:
            q = deque([v])
            c = 1
            cy = set()
            while q:
                n = len(q)
                node = q.popleft()
                cy.add(node)
                if len(graph[node]) != 2:
                    c =0
                for child in graph[node]:
                    if child not in visited:
                        q.append(child)
                        visited.add(child)
            if c:
                cycles.append(list(cy))
    return(len(cycles))


    


# for _ in range(int(input())):
print(sol())
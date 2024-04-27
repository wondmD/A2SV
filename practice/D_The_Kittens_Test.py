from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right


def find(x):
    if x == parent[x]:
        return x
    return find(parent[x])
def union(x,y):
    parent_x = find(x)
    parent_y = find(y)

    if parent_x != parent_y:
        if rank[parent_x] >= rank[parent_y]:
            ch[parent_x].append(y)
            parent[parent_y] = parent_x
            rank[parent_x] += 1
        else:
            ch[parent_y].append(x)
            parent[parent_x] = parent_y
            rank[parent_y] += 1
num = int(stdin.readline())
parent = {i+1:i+1 for i in range(num)}
ch = {i+1:[i+1] for i in range(num)}
rank = {i+1:i+1 for i in range(num)}
vi = set()
ans = []
def dfs(node):
    if node not in graph:
        ans.append(node)
        vi.add(node)
    for i in graph[node]:
        if i not in vi:
            dfs(i)
            # vi.add(i)
        
graph = defaultdict(set)

for i in range(num-1):
    a, b= map(int, stdin.readline().split())
    graph[a].add(b)

for i in range(1,num+1):
    if i not in graph:
        ans.append(i)
    elif i not in vi:
        dfs(i)
print(ans)
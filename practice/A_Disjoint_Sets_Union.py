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
            parent[parent_y] = parent_x
            rank[parent_x] += 1
        else:
            parent[parent_x] = parent_y
            rank[parent_y] += 1
a, b= map(int, stdin.readline().split())
parent = {i:i for i in range(1, a+1)}

rank = {i:1 for i in range(1, a+1)}

for i in range(b):
    cmd, x,y = input().split()
    if cmd == 'union':
        union(int(x), int(y))
    else:
        print('YES' if find(int(x)) == find(int(y)) else 'NO')


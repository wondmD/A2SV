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
            when[y] = exp[parent_y]
            parent[parent_y] = parent_x
            rank[parent_x] += 1
        else:
            when[x] = exp[parent_x]
            parent[parent_x] = parent_y
            rank[parent_y] += 1
a, b= map(int, stdin.readline().split())
parent = {i:i for i in range(1, a+1)}
exp = {i:0 for i in range(1, a+1)}
when = {i:0 for i in range(1, a+1)}
rank = {i:1 for i in range(1, a+1)}

for i in range(b):
    cmd = input().split()
    if cmd[0] == 'join':
        union(int(cmd[1]), int(cmd[2]))
    elif cmd[0] == 'add':
        par = find(int(cmd[1]))
        exp[par] += int(cmd[2])
    else:
        par = find(int(cmd[1]))
        print(exp[par] - when[int(cmd[1])])
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
            mmn[parent_x][0] = min(mmn[parent_x][0], mmn[parent_y][0])
            mmn[parent_x][1] = max(mmn[parent_x][1], mmn[parent_y][1])
            mmn[parent_x][2] += mmn[parent_y][2]
            parent[parent_y] = parent_x
            rank[parent_x] += 1
        else:
            mmn[parent_y][0] = min(mmn[parent_x][0], mmn[parent_y][0])
            mmn[parent_y][1] = max(mmn[parent_x][1], mmn[parent_y][1])
            mmn[parent_y][2] += mmn[parent_x][2]
            parent[parent_x] = parent_y
            rank[parent_y] += 1
a, b= map(int, stdin.readline().split())
parent = {i:i for i in range(1, a+1)}
mmn = {i:[i,i,1] for i in range(1,a+1)}
rank = {i:1 for i in range(1, a+1)}

for i in range(b):
    cmd= list(input().split())
    if cmd[0] == 'union':
        union(int(cmd[1]), int(cmd[2]))
    else:
        idx = find(int(cmd[1]))
        print(mmn[idx][0],mmn[idx][1],mmn[idx][2])


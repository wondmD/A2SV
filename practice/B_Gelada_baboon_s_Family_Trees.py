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
a= int(input())
lis = list(map(int, stdin.readline().split()))
parent = {i:i for i in range(1, a+1)}

rank = {i:1 for i in range(1, a+1)}

for i in range(a):
    union(i+1, lis[i])
ans = set()
for i in lis:
    ans.add(find(i))
print(len(ans))
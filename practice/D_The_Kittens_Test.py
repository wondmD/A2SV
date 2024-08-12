from sys import stdin
def find(x):
    if x == parent[x]:
        return x
    return find(parent[x])
def union(x,y):
    parent_x = find(x)
    parent_y = find(y)

    if parent_x != parent_y:
        if size[parent_x] >= size[parent_y]:
            parent[parent_y] = parent_x
            lists[parent_x].extend(lists[parent_y])
            size[parent_x] += size[parent_y]
        else:
            parent[parent_x] = parent_y
            lists[parent_y].extend(lists[parent_x])
            size[parent_y] += size[parent_x]

        
a = int(input())
parent = {i:i for i in range(1, a+1)}
lists = {i:[i] for i in range(1, a+1)}
size = {i:1 for i in range(1, a+1)}

for i in range(a-1):
    x,y= map(int, stdin.readline().split())
    union(x,y)
print(*lists[find(1)])

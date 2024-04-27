from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

def sol():
    n ,m= map(int, stdin.readline().split())
    graph = defaultdict(list)
    for i in range(m):
        a, b= map(int, stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    d = defaultdict(int)
    l = []
    for i in graph:
        d[len(graph[i])]+=1
    x = 0
    for i in d:
        if d[i] == 1:
            x = i
            break
    y = 0
    if not x:
        for i in d:
            x = y = i
    else:
        for i in d:
            if d[i] == x:
                y = i
                break
    return (x,y-1)

for _ in range(int(input())):
    print(*sol())
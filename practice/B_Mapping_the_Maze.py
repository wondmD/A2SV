from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

def sol():
    n, m= map(int, stdin.readline().split())
    graph = defaultdict(list)

    for i in range(m):
        a, b= map(int, stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    star = False
    bedge = 0
    another = 0
    # print(graph)
    for i in graph:
        x = len(graph[i]) 
        if x== n-1:
            star= True
        elif x== 1:
            bedge += 1
        elif x== 2:
            another += 1
    if bedge == 2 and another == n-2:
        return 'bus topology'
    elif another == n:
        return 'ring topology'
    if star and bedge == n-1:
        return 'star topology'
    return 'unknown topology'
    



# for _ in range(int(input())):
print(sol())
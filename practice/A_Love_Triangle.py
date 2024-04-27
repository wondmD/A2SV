from sys import stdin
from collections import defaultdict, deque
# from bisect import bisect_left, bisect_right

def sol():
    num = int(stdin.readline())
    lis = list(map(int, stdin.readline().split()))
    graph = defaultdict(list)
    for i in range(num):
        graph[i+1] = lis[i]
    # print(graph)
    for x in graph:
        
        path = [x]
        # print(path)
        for i in range(3):
            
            if path[-1] not in graph:
                break
            path.append(graph[path[-1]])
        if path[-1] == x:
            return 'YES'
        # print(path)
    return 'NO'

# for _ in range(int(input())):
print(sol())
from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

def sol():
    num = int(stdin.readline())
    lis = list(map(int, stdin.readline().split()))
    s = stdin.readline()
    graph = defaultdict(list)
    for i in range(num-1):
        graph[lis[i]].append((i+2,0,0))
    q = deque([1])
    while q:
        n = len(q)
        


for _ in range(int(input())):
    print(sol())
from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right




def sol():
    n = int(stdin.readline())
    s = []
    for _ in range(n):
        s.append(stdin.readline().strip())

    graph = defaultdict(list)
    indegree = [0] * 26
   

sol()
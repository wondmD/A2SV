
from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

def sol():
    l = []
    a = "abcdefghijklmnopqrstuvwxyz"
    graph = defaultdict(list)
    num = int(stdin.readline())
    prev = stdin.readline().strip()
    for i in range(num-1):
        s = stdin.readline().strip()
        p =0
        while p < min(len(s), len(prev)) and s[p] == prev[p]:
            p += 1
        if p < len(prev) and p < len(s):
            if s[p] < prev[p]:
                graph[prev[p]] = s[p]
        prev = s
    return graph
# for _ in range(int(input())):
print(sol())

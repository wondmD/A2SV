from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right


d = defaultdict(int)
for _ in range(int(input())):
    d[input()] += 1
p = []
for i in d:
    p.append((d[i],i))
p.sort()
print(p[-1][1])
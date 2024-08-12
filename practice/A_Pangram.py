from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

num = int(stdin.readline())
s = stdin.readline().strip()

d = {}
for i in s:
    if i.lower() not in d:
        d[i.lower()] = 1
    else:
        d[i.lower()]+=1
# print(d)
if len(d) == 26:
    print('YES')
else:
    print('NO')

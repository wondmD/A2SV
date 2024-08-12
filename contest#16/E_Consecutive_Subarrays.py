from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

n,k= map(int, stdin.readline().split())
lis = list(map(int, stdin.readline().split()))

ps = []
for i in range(n-1, -1, -1):
    if ps:
        ps.append(ps[-1] + lis[i])
    else:
        ps = [lis[i]]
ans = ps.pop()
ps.sort()
for i in range(k-1):
    ans += ps.pop()
    
print(ans)
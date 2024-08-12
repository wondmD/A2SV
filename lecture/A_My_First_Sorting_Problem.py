from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

def sol():
    a, b= map(int, stdin.readline().split())
    return min(a,b), max(a,b)

for _ in range(int(input())):
    ans = sol()
    print(ans[0], ans[1])

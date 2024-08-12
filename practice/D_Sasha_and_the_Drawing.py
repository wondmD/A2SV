from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right
from math import ceil

def sol():
    a, b= map(int, stdin.readline().split())
    ans = 0
    if (4*a -2) == b:
        ans = (b//2)+1
    else:
        ans = ceil(b/2)
    return ans

for _ in range(int(input())):
    print(sol())

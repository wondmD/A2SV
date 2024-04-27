from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

def sol():
    n = int(stdin.readline())
    lis = list(map(int, stdin.readline().split()))
    lis.sort()
    for i in range(1, n):
        if lis[i] - lis[i-1] > 1:
            return "NO"
    return "YES"
for _ in range(int(input())):
    print(sol())
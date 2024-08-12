from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right
from math import ceil

def sol():
    a, b= map(int, stdin.readline().split())
    lis = list(map(int, stdin.readline().split()))
    lis2 = [(ceil(lis[i]/b), i+1) for i in range(len(lis))]
    lis2.sort()
    return lis2[-1][1]

# for _ in range(int(input())):
print(sol())
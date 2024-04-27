from sys import stdin
from collections import defaultdict, deque, Counter
from bisect import bisect_left, bisect_right



def sol():
    lis = list(map(int, stdin.readline().split()))
    x = Counter(lis)
    if lis[0] < lis[1] and lis[1] < lis[2]:
        return 'STAIR'
    elif lis[0] < lis[1] and lis[1] > lis[2]:
        return 'PEAK'
    else:
        return 'NONE'

for _ in range(int(input())):
    print(sol())
from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

def sol():
    # pass
    n = int(stdin.readline())
    l1 = list(map(int, stdin.readline().split()))
    m = int(stdin.readline())
    l2 = list(map(int, stdin.readline().split()))
    l1.sort()
    l2.sort()
    p1 = 0
    p2 = 0
    c = 0
    while p1 < len(l1) and p2 < len(l2):
        if abs(l1[p1]- l2[p2]) <= 1:
            c += 1
            p1+=1
            p2+=1
        elif l1[p1] < l2[p2]:
            p1+=1
        else:
            p2+=1
    return c

# for _ in range(int(input())):
print(sol())
from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

def sol():
    num = int(stdin.readline())
    lis = list(map(int, stdin.readline().split()))
   
    p1 = 0 
    p2 = num-1
    ans = 0
    while p1 < p2:
        if lis[p1] == lis[p2]:
            ans = max(ans, (p1+1+(num-p2)))
            p1 += 1
            lis[p1] += lis[p1-1]
            p2 -= 1
            lis[p2] += lis[p2+1]
        elif lis[p1]< lis[p2]:
            p1 += 1
            lis[p1] += lis[p1-1]
        else:
            p2 -= 1
            lis[p2] += lis[p2+1]
    return ans


for _ in range(int(input())):
    print(sol())
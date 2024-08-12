from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right
from math import gcd

def sol():
    num = int(stdin.readline())
    lis = list(map(int, stdin.readline().split()))
    l1 = l2 =[]
    for i in lis:
        if i%2:
            l2.append(i)
        else:
            l1.append(i)
    l1.sort(reverse=True)
    l2.sort(reverse=True)
    lis = l1 + l2
    ans = 0

    for i in range(num-1):
        for j in range(i+1, num):
            if gcd(lis[i], 2*lis[j]) > 1:
                ans += 1
    return ans

for _ in range(int(input())):
    print(sol())

from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

def sol():
    num = int(stdin.readline())
    lis = list(map(int, stdin.readline().split()))
    lis.sort()
    a=b=0
    for i in lis:
        if a<=b:
            a+=i
        else:
            b+=i
    if a == b:
        return 'YES'
    return 'NO'

for _ in range(int(input())):
    print(sol())
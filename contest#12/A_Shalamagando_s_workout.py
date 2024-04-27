from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

def sol():
    # pass
    num = int(stdin.readline())
    lis = list(map(int, stdin.readline().split()))
    c= b=ba = 0
    l = 0
    for i in range(0, num, 3):
        c += lis[i]
    for i in range(1, num, 3):
        b += lis[i]
    for i in range(2, num, 3):
        ba += lis[i]
    max_= max(c, b, ba)
    if max_ == c:
        return 'chest'
    elif max_ == b:
        return 'biceps'
    else:
        return 'back'




# for _ in range(int(input())):
print(sol())
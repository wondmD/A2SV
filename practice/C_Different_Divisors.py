from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right


def sol():
    num = int(stdin.readline())
    x = num+1
    y = x+num
    return(x*2)

for _ in range(int(input())):
    print(sol())
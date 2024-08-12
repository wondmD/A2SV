from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

def sol():
    a, b,c= map(int, stdin.readline().split())
    if c/2 >= b:
        return a*b
    else:
        if a%2:
            return ((a//2 )*c) + b
        else:
            return (a//2 )*c

for _ in range(int(input())):
    print(sol())
from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

def sol():
    a, b= map(int, stdin.readline().split())
    l = []
    for i in range(a):
        l.append(chr(ord('a') + (i%b)))
    return(''.join(l))

for _ in range(int(input())):
    print(sol())
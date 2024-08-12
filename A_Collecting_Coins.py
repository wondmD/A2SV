from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

def sol():
    a, b,c,d= map(int, stdin.readline().split())
    x = max(a,b,c)
    y = a+b+c+d
    if y%3==0 and y//3 >= x:
        return 'YES'
    return 'NO'

for _ in range(int(input())):
    print(sol())
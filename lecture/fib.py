from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

d = defaultdict(int)
def fib(n):
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n not in d:
        d[n] = fib(n-1) + fib(n-2)
    return d[n]
print(fib(99))
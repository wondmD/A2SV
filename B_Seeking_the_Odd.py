from sys import stdin
# from collections import defaultdict, deque
# from bisect import bisect_left, bisect_right
from math import sqrt
def sol():
    num = int(stdin.readline())
    if num %2:
        return 'YES'
    while num > 2:
        if num%2:
            return "YES"
        num //= 2
    return 'NO'
for _ in range(int(input())):
    print(sol())
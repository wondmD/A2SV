from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

def sol():
    s = stdin.readline().strip()
    ans = s + s[::-1]
    return ans

for _ in range(int(input())):
    print(sol())
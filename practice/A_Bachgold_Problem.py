from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

def sol():
    num = int(stdin.readline())
    if num%2==0:
        print(num//2)
        print (*[2 for i in range(num//2)])
    else:
        print(num//2)
        ans = [2 for i in range(num//2 -1)]+[3]
        print(*ans)
sol()

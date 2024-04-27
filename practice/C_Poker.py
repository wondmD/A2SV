from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right
import heapq

def sol():
    num = int(stdin.readline())
    lis = list(map(int, stdin.readline().split()))
    heap = []
    ans = 0
    for i in lis:
        if i != 0:

            heapq.heappush(heap, -i)
        else:
            if heap:
                ans -= heapq.heappop(heap)
    return ans
for _ in range(int(input())):
    print(sol())
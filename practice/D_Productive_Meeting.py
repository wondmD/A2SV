from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right
import heapq as h

def sol():
    num = int(stdin.readline())
    lis = list(map(int, stdin.readline().split()))
    lis2 = [(-lis[i],i+1) for i in range(num) if lis[i] > 0]
    ans = []
    h.heapify(lis2)
    
    while len(lis2) > 1:
        x = h.heappop(lis2)
        y = h.heappop((lis2))
        ans.append([min(x[1], y[1]), max(x[1], y[1])])
        # print(x, y, '[[]]')
        if -1 * x[0] - 1 > 0:
            h.heappush(lis2,(x[0]+1, x[1]))
        if -1 * y[0] - 1 > 0:
            h.heappush(lis2,(y[0]+1, y[1]))

        # print(lis2)

    return ans
for _ in range(int(input())):
    x = sol()
    print(len(x))
    for p in (x):
        print(*p)
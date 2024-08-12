from sys import stdin
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify

from bisect import bisect_left, bisect_right

import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    num = int(stdin.readline())
    lis = list(map(int, stdin.readline().split()))
    all = set(lis)
    dp = defaultdict(int)
    def find(n, col):
        col.add(n)
        col.add(n-1)
        col.add(n+1)
        if n not in all:
            return 0
        if n in dp:
            return dp[n]
        cur = n
        c = 0
        for i in lis:
            if i not in col:
                c = 1
                cur = max(cur, find(i, col))
                print(cur,"here")
        dp[n] = cur
        return (dp[n])
    ans = 0
    for i in lis:
        ans = (max(ans, find(i, set())))
    print(ans)
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()


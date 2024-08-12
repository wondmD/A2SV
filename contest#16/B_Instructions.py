from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():

    def sol():
        num = int(stdin.readline())
        lis = list(map(int, stdin.readline().split()))
        dp = defaultdict(int)
        def find(idx):
            if idx >= num:
                return 0
            if idx in dp:
                return dp[idx]
            dp[idx] = lis[idx] + find(idx + lis[idx])
            return dp[idx]
        ans = 0
        for i in range(num):
            ans = max(ans, find(i))
        return ans
    for _ in range(int(input())):
        print(sol())
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()

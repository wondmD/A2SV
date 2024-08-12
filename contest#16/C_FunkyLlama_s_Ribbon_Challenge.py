from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    def sol():
        org, a, b, c = map(int, stdin.readline().split())
        cuttings = [a, b,c]
        dp ={}
        def find(n):
            if n ==0:
                return 0
            if n in dp:
                return dp[n]
            cur = float('-inf')
            for i in cuttings:
                if i <= n:
                    cur = max(cur, 1+find(n-i))
            dp[n] = cur
            return dp[n]   
        return find(org) 
    # for _ in range(int(input())):
    print(sol())

    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()


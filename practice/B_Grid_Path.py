# from functools import cache
from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    def sol():
        n,m,k= map(int, stdin.readline().split())
        memo ={}
        def find(i,j,bur):
            # print(i,j)
            if i > n or j > m:
                return False
            if i == n and j == m and bur ==k:
                return True
            if (i,j,bur) in memo:
                return memo[(i,j,bur)]
            movx = find(i,j+1, bur+i)
            movy = find(i+1,j, bur+j)

            memo[(i,j,bur)] = movx or movy
            return memo[(i,j,bur)]
        if find(1,1,0):
            return 'YES'
        else:
            return 'NO'
    
    for _ in range(int(input())):
        print(sol())
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()

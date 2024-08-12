from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    # write your solution here
    def sol():
        s = input()
        n = len(s)
        ans = n
        for i in range(n):
            for j in range(i + 1, n):
                val = int(s[i] + s[j])
                # print(val)
                if val % 25 == 0:
                    ans = min(ans, n - i - 2)
        return ans
        
    for _ in range(int(input())):
        print(sol())
   
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()

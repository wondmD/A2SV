from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    num = int(stdin.readline())
    lis = list(map(int, stdin.readline().split()))
    
    def method(left, right):
        if left == right:
            return lis[left]
        mid = (left + right) // 2
        return max(method(left, mid), method(mid + 1, right))
    


    pass
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()

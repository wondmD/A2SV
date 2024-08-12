import math
import sys


import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())

    nums = list(map(int, input().split()))
    mem = {}

    def recur(idx, prev):
        if idx >= n:
            return 0
        
        if (idx, prev) not in mem:
            take = 0
            
            if prev == -1 or  (nums[idx] > nums[prev] and math.gcd(nums[idx], nums[prev]) > 1):
                take = 1 + recur(idx + 1, idx)

            not_take = recur(idx+1, prev)

            mem[(idx, prev)] = max(take, not_take)

        return mem[(idx, prev)]
    
    print(recur(0, -1))
    pass
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()


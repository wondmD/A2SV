from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    


    def sol():
        MOD = (10 ** 9) +7
        amount = int(stdin.readline())
        coins = [i for i in range(1, 4 * (10**4)) if is_pal[i]]
        memo = [[-1 for _ in range(amount+1)] for _ in range(len(coins)+1)]

        def find_coin(idx, sum_):
            if idx >= len(coins) or sum_ > amount:
                return 0
            if sum_ == amount:
                return 1
            if sum_ > amount:
                return 0
            if memo[idx][sum_] <0:
                include = 0
                if sum_+coins[idx] <= amount:
                    include = find_coin(idx, sum_+coins[idx])
                exclude = find_coin(idx+1, sum_)
                memo[idx][sum_]  =  include+exclude
            return memo[idx][sum_] 
        # print(memo)
        return find_coin(0,0)%MOD

    is_pal ={}
    
    for i in range(1, 4 * (10**4)):
        x = str(i)
        if x == x[::-1]:
            is_pal[i] = True
        else:
            is_pal[i] = False
    # print(len(is_pal))
    for _ in range(int(input())):
        print(sol())
        
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()

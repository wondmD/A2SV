import sys, threading
from collections import Counter

input = lambda: sys.stdin.readline().strip()

def main():
    memo = {}
    n = int(input())
    cnt = Counter(map(int,input().split()))
    def dp(n):

        if n <= 1:
            return cnt[n]
        if n not in memo:
            memo[n] = max(dp(n -1), dp(n -2) + cnt[n]*n)
    	
        return memo[n]
    print(dp(max(cnt.keys())))
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()

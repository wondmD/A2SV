from sys import stdin
from collections import defaultdict, deque, Counter
from bisect import bisect_left, bisect_right

def sol():    
    n = int(input())
    a = list(map(int, input().split()))
    
    if a.count(a[0]) == n:
        return(-1)
    else:
        ans = float('inf')
        cnt = 0
        
        for i in range(n):
            if a[i] == a[0]:
                cnt += 1
            else:
                ans = min(ans, cnt)
                cnt = 0
        
        ans = min(ans, cnt)
        return(ans)
                    
for _ in range(int(input())):
    print(sol())
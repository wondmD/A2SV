from sys import stdin
from bisect import insort
# from collections import defaultdict, deque
# from bisect import bisect_left, bisect_right
import math


def sol():
    a, k= map(int, stdin.readline().split())
    lis = list(map(int, stdin.readline().split()))
    if a == 1:
        return 0
    lis[0] -= k
    for i in range(1, a):
        lis[i] -= k
        if 0 <= lis[i-1] <= lis[i] <= float('inf'):


        if nums[]

    gcd_num = math.gcd(*lis)
    for i in range(a):
        lis[i] //= gcd_num
        lis[i] -= 1 
    
    ans = sum(lis)


    return ans
    # for i in range(1,a):
    #     lis[i]-= k
    #     if 
        
    # gcd = lis[0]
    # for i in range(1,a):
    #     gcd = math.gcd(gcd, lis[i]-k)
    # ans = 0
    # # print(gcd, "gcd")
    # for i in range(a):
    #     ans += (lis[i]-k//gcd) -1
    # return ans

for _ in range(int(input())):
    
    print(sol())
from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

def sol():
    num = int(stdin.readline())
    lis = list(map(int, stdin.readline().split()))
    xor_l = []
    xor_r = []
    max_ = 0
    xor = 0
    for i in range(num):
        xor ^= lis[i]
        max_ = max(max_, xor)
        xor_l.append(max_)
    xor = 0
    for i in range(num-1, -1, -1):
        xor ^= lis[i]
        max_ = max(max_, xor)
        xor_r.append(max_)
    ans = max(xor_l[-1],xor_r[-1])
    for i in range(num):
        ans = max(ans, xor_l[i] , xor_r[num-1-i])
  
    return ans
print(sol())

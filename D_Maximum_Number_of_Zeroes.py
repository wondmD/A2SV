from sys import stdin
# from collections import defaultdict, deque
# from bisect import bisect_left, bisect_right
from fractions import Fraction
def sol():
    num = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    b = list(map(int, stdin.readline().split()))
    d = {}
    zs = 0
    for i in range(num):
        if a[i] == 0 or b[i] == 0:
            if a[i] == 0 and b[i] == 0:
                zs += 1
            elif b[i]==0:
                d[0]=d.get(0, 0)+1
            continue
        x = Fraction(a[i], b[i])
        d[x]= d.get(x, 0) + 1
    ans = 0
    # print(d)
    for i in d:
        ans = max(ans, d[i])
    return ans + zs
        

print(sol())
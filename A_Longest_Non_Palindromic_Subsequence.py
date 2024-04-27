from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right
import math
def sol():
    s = input().strip()
    n= len(s)
    # print(s[::-1])
    if s != s[::-1]:
        return n
 
    for i in range(math.ceil(n/2)):
        if s[i:] != s[i:][::-1]:
            return n-i
        if s[i] != s[-1]  and s[i:]:
            
            return n-i 
        
    return(-1)
for _ in range(int(input())):
    print(sol())
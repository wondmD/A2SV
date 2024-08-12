from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

def sol():
    a, b= map(int, stdin.readline().split())
    if a ==1:
        return b
    
    x = a//2 +1
    return b//x
  

    

for _ in range(int(input())):
    print(sol())
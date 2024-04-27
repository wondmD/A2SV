from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

def sol():
    num = int(stdin.readline())
    s = list(stdin.readline().strip())
    lis = list(map(int, stdin.readline().split()))
    ref = list(range(1,num+1))
    
    q = deque(s)
    while q  != s:
        temp = q[:]
        for i in range(num):
            pass

        

for _ in range(int(input())):
    print(sol())
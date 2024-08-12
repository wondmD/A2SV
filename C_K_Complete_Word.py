from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

def sol():
    a, b= map(int, stdin.readline().split())
    s = stdin.readline().strip()
    dic = defaultdict(defaultdict[int])
    for i in range(a):
        dic[(i+1)%b][s[i]] += 1
    
    return (dic)

for _ in range(int(input())):
    print(sol())
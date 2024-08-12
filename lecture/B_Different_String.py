from sys import stdin
from collections import defaultdict, deque, Counter
from bisect import bisect_left, bisect_right

def sol():
    s = stdin.readline().strip()
    if len(Counter(s)) <= 1:
        return 'NO'
    s = list(s)
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            s[i], s[i+1] = s[i+1],s[i]
    print('YES')
    return "".join(s)

for _ in range(int(input())):
    print(sol())

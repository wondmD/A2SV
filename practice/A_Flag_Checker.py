from sys import stdin
from collections import defaultdict, deque, Counter
# from bisect import bisect_left, bisect_right

def sol():
    a, b= map(int, stdin.readline().split())
    # d = defaultdict(int)
    prev = None
    for i in range(a):
        s = stdin.readline().strip()
        x = Counter(s)
        # print(x)
        if len(x) > 1:
            return 'NO'
        elif s[0] == prev:
            return 'NO'
        else:
            prev = s[0]
    return 'YES'

# for _ in range(int(input())):
print(sol())
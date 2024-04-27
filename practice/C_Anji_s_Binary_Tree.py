from sys import stdin
from collections import defaultdict, deque, Counter
# from bisect import bisect_left, bisect_right

def is_p(n):
    d = 2
    while d*d <= n:
        if n%d:
            return False
    return True
def sol():
    num = int(stdin.readline())
    lis = list(map(int, stdin.readline().split()))
    d = defaultdict(int)

    for x in lis:
        st = 2
        while x > 2:
            if x%st == 0:
                x //=st
                d[st] += 1
            else:
                st+=1
                while not is_p(st):
                    st+=1
    x = Counter(list(d.values()))
    return len(x) == 1



for _ in range(int(input())):
    print(sol())
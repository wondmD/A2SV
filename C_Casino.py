from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right


num = int(stdin.readline())
lis = list(map(int, stdin.readline().split()))
lis.sort()
x = lis[0]
while True:
    if x % 3 == 0:
        x //=3
    elif x % 2 == 0:
        x //=2
    else:
        break
ans = 'Yes'
for i in range(num):
    f = 0
    while True:
        if lis[i] % 3 == 0:
            lis[i] //=3
        elif lis[i] % 2 == 0:
            lis[i] //=2
        else:
            if lis[i] != x:
                f = 1
            break
    if f == 1:
        ans = 'No'
        break
print(ans)
from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

num = int(stdin.readline())

lis = list(map(int, stdin.readline().split()))


sum_ = []
c = 1
for i in range(num-1):
    if lis[i] == lis[i+1]:
        c+=1
    else:
        sum_.append(c)
        c = 1
sum_.append(c)
if len(sum_) == 1:
    print(0)
else:
    ans = 0
    for i in range(len(sum_)-1):
        ans =max(ans, min(sum_[i], sum_[i+1]))
    print(ans*2)
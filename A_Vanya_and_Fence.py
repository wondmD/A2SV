from sys import stdin
# from collections import defaultdict, deque
# from bisect import bisect_left, bisect_right

a, b= map(int, stdin.readline().split())
lis = list(map(int, stdin.readline().split()))
c = 0
for i in lis:
    if i > b:
        c+=1
print (a+c)
from sys import stdin
# from collections import defaultdict, deque
# from bisect import bisect_left, bisect_right


for _ in range(int(input())):
    n, k= map(int, stdin.readline().split())
    if n==k:
        print(0)
    else:

        print (max(((n-(k+1))*3 +1 + ((k-1)//2)*3 + ((k-1)%2)),0))
    
from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    print (max(l) -min(l))

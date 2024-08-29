n, p, v = map(int, input().split())
lis = list(map(int, input().split()))
lis.sort()
print(lis[n-p] - lis[n-p-1])

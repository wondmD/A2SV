n = int(input())
lis = list(map(int,input().split()))[:n]
lis.sort()
for i in lis:
    print(i, end=" ")
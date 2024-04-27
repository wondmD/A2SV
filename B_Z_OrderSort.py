n = int(input())
my = list(map(int, input().split()))
result = []
my.sort()
f =0
l = 0
r = n-1
while (len(result)<n):
    if f == 0:
        result.append(my[l])
        l+=1
        f =1
    else:
        result.append(my[r])
        r-=1
        f=0
for i in result:
    print(i, end=" ")
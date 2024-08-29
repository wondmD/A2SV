n = int(input())
lis  = list(map(int, input().split()))
last1 =lis[-1]
last2 = 0
ans  =[lis[-1]]
lis.reverse()
for i in range(1, n):
    curr = lis[i] +last1 -last2
    x = last2
    last2 = last1
    last1 = x+curr
    ans.append(curr)
ans.reverse()
print(*ans)

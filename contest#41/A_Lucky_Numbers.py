n, k = map(int, input().split())
lis = list(map(int, input().split()))

ans =0
for num in lis:
    s= str(num)
    lucky = s.count('4')+s.count('7')
    if lucky <= k:
        ans +=1
print(ans)
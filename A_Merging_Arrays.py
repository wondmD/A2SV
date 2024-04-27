n, m = map(int, input().split())
ln = list(map(int, input().split()))
lm = list(map(int, input().split()))

np = 0
mp =0

result = []
while (np<n and mp<m):
    if ln[np] <= lm[mp]:
        result.append(ln[np])
        np+=1
    else:
        result.append(lm[mp])
        mp+=1
if np < n:
    result += ln[np:]
elif mp < m:
    result += lm[mp:]
for i in result:
    print (i, end=' ')
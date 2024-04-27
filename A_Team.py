
tc = int(input())
ans = 0
for _ in range(tc):
    p, v, t= map(int, input().split())
    tot = p + v + t
    if tot >= 2:
        ans += 1
print(ans)

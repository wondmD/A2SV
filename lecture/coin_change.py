import math

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    ans = 0
    mp = {}
    lis = list(map(int,input().split()))
    for i in range(n):
        x = lis[i]
        for i in range(31):
            if x & 1:
                if i in mp:
                    mp[i] += 1
                else:
                    mp[i] = 1
            x >>= 1

    for i in range(30, -1, -1):
        y = n - mp.get(i, 0)
        if k >= y:
            ans += 2**i
            k -= y

    print(ans)
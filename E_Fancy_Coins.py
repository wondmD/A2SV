import math
for _ in range(int(input())):
    m,k,a1,ak = map(int, input().split())
    f = 0
    for i in range(k+1):
        if m < i*k and m >= a1 +(i*k):
            print(0)
            f = 1
    if f == 0:
        _sum = a1 + (k * ak)
        d = m - _sum
        ans = 0
        x = d // k
        _sum += x * k
        d -=(x*k)
        if a1 >k :
            ans += 1
        else:
            ans += d
        print(x+ans)

        
        
        
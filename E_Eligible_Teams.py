for _ in range(int(input())):
    n , x = map(int, input().split())
    lis = list(map(int, input().split()))
    lis.sort(reverse=True)
    res = 0
    r=0
    l = 0
    while r < n:
        if ((r - l)+1) * lis[r] >= x:
            res += 1
            l = r = r+1
        else:
            r += 1
    print(res)

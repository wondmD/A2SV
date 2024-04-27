for tc in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    x = sorted(l)
    m1 = x[-1]
    m2 = x[-2]
    res = []
    for i in l:
        if i != m1:
            res.append(i-m1)
        else:
            res.append(i-m2)
    print(*res)
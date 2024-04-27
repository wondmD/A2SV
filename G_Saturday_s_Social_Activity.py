for _ in range(int(input())):
    n  = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    l = []
    for i in range(n):
        l.append([a[i],b[i],a[i]+b[i]])
    l.sort(key=lambda x:x[2], reverse=True)
    res = 0
    for i in range(n):
        if i % 2 ==0:
            res += (l[i][0]-1)
        else:
            res -= l[i][1]-1
    print(res)
for _ in range(int(input())):
    n  = int(input())
    l = list(map(int, input().split()))
    lc = 1
    rc = 1
    for i in range(1,n):
        if l[i] == l[i-1]:
            lc+=1
        else:
            break
    for i in range(n-2, -1, -1):
        if l[i] == l[i+1]:
            rc+=1
        else:
            break
    if lc==n or rc == n:
        print(0)
    elif l[-1] != l[0]:
        print (n - max(lc,rc))
    else:
        print (n - (lc +rc))
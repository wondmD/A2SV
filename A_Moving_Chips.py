for _ in range(int(input())):
    n  = int(input())
    l = list(map(int, input().split()))

    oc = l.count(1)
    f_1 = 0
    res = 0
    for i in range(n):
        if l[i] == 1:
            f_1 = i
            break

    c = 0
    for i in range(f_1,n):
        
        if l[i] == 0:
            c+=1
        else:
            res += c
            c = 0
    print (res)

n = int(input())
l = list(map(int, input().split()))
if len(set(l)) == n:
    print(0)
else :
    l2 = []
    p1 = 0
    p2 = n-1
    for i in range(n):
        if l[i] in l2 :
            p1=i
            break
        else :
            l2.append(l[i])
    for i in range(n-1,p1-1,-1):
        if l[i] in  l2:
            p2 = i
            break
        else:
            l2.append(l[i])
    print (n-len(set(l[:p1]+l[p2+1:])))
    

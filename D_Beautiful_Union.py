from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if n==1 and a[0] == b[0]:
        print (2)
        continue
    if n==1:
        print (1)
        continue
    dic1 = defaultdict(int)
    dic2 = defaultdict(int)
    c = 1
    for i in range(1,n):
        if a[i] == a[i-1]:
            c+=1
        else:
            dic1[a[i-1]] = max(dic1[a[i-1]], c)
            c = 1
        if i == n-1:
            dic1[a[i]] = max(dic1[a[i]], c)
    c = 1
    for i in range(1,n):

        if b[i] == b[i-1]:
            c+=1
        else:
            dic2[b[i-1]] = max(dic2[b[i-1]], c)
            c = 1
        if i == n-1:
            dic2[b[i]] = max(dic2[b[i]], c)
    max_ =0 
    for i in dic1:
        max_ = max(max_, dic1[i] + dic2[i])
    for i in dic2:
        max_ = max(max_, dic1[i] + dic2[i])
    print (max_)
    
l, r= map(int, input().split())
flag = False
m=str(l)
k=[]
for i in m:
    if i in k:
        continue
    else:
        k.append(i)
    t="".join(k)
if len(k)==len(m):
    flag = True
    print(m)
else:
    while l<r:
        l+=1
        m=str(l)
        k=[]
        for i in m:
            if i in k:
                continue
            else:
                k.append(i)
            t="".join(k)
        if len(k)==len(m):
            flag = True
            print(m)
            break

if len(k)<len(m):
    flag = True
    print("-1")
n = int(input())
l = list(map(int, input().split()))
l.sort()
c = 0
p1 = 0
p2 = 0
while (p2 < n):
    if l[p1] < l[p2]:
        c+=1
        p1+=1
        p2+=1
    else :
        p2+=1
print(c)
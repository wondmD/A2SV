n = int(input())
l = list(map(int, input().split()))
w = 0
l.sort()
c = 0
for i in range(n):
    if l[i] >= w:
        c+=1
        w+=l[i]

print(c)
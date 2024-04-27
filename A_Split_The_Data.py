n = int(input())
size = int(input())
l = []
for i in range(n):
    l.append(int(input()))
l.sort(reverse=True)
s = 0
x = 0
leng = len(l)
while s< size and x < leng:
    s+=l[x]
    x+=1
print(x)
l = []
for i in range(5):
    l.append(list(map(int, input().split())))
x = 0
y =0
f = 0
for i in range(5):
    for j in range(5):
        if l[i][j] == 1:
            x = i+1
            y = j+1
            f = 1
            break
    if f==1:
        break
print (abs(x-3)+abs(y-3))
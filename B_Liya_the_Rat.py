from sys import stdin
s = stdin.readline()
y = len(s)
n = int(stdin.readline())
p = [0]

for i in range(y-1):
    if s[i] == s[i+1]:
        p.append(p[-1]+1)
    else:
        p.append(p[-1])

for i in range(n):
    a, b= map(int, input().split())
    print(p[b-1]- p[a-1])

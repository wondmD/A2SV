def sol():
    n, m = map(int, input().split())
    s = input()
    c = input()
    prefix = [0,ord(s[0])]
    for i in range(1, n):
        prefix.append(prefix[-1] + ord(s[i]))
    tot = 0
    for i in c:
        tot+= ord(i)
    p = m
    while p <=n:
        if tot == prefix[p] - prefix[p-m]:
            return "YES"
        p+=1
    return 'NO'

for _ in range(int(input())):
    print(sol())
    
    
    
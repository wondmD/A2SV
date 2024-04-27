from collections import Counter
l , r = map(int, input().split())

def check (num):
    s = str(num)
    c = Counter(s)
    if len(c) == len(s):
        return (True)
    return (False)
v = -1
for i in range(l,r+1):
    if check(i):
        v  = i
        break
print(v)
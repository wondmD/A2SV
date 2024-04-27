from collections import defaultdict
from fractions import Fraction
n = int(input()) 
a = list(map(int, input().split()))
b = list(map(int, input().split())) 
c = defaultdict(int) 
d = 0   
for i in range(n):
    if b[i] == 0 and a[i] == 0:
        d += 1
    elif a[i]:
        fraction = Fraction(-b[i], a[i])
        c[fraction] += 1

d += max(c.values()) if c else 0
print(d)


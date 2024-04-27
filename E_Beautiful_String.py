n, k  = map(int, input().split())
s = input()

lptr = 0
b = 0
max_len = 1


for right in range(n):
    if s[right] == 'b':
        b += 1


    while b > k:
        if s[lptr] == 'b':
            b -= 1
        lptr += 1

    max_len = max(max_len, right - lptr + 1)

lptr = 0
a = 0

for right in range(n):
    if s[right] == 'a':
        a += 1

    while a > k:
        if s[lptr] == 'a':
            a -= 1
        lptr += 1

    max_len = max(max_len, right - lptr + 1)

print(max_len)
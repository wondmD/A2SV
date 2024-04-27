n = int(input())
s = list(input())

for i in range(n):
    if n % (i+1) == 0:
        l = 0
        r = i
        while l <= r:
            s[l], s[r] = s[r], s[l]
            l+=1
            r-=1
print("".join(s)) 
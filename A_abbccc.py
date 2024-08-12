num = int(input())
s = input()

idx = 0
inc = 1
ans =""
while idx < num:
    ans += s[idx]
    idx += inc
    inc+=1
print(ans)
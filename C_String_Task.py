s = input()
vs = 'aeiouy'
ans = []
for i in s:
    if i.lower() not in vs:
        ans.append('.' + i.lower())
print("".join(ans))



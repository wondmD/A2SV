from collections import Counter


def sol():
    leng= int(input())
    s = input()
    c = Counter(s)
    ans = []
    ss = "bugyrt"
    for i in ss:
        if i in c:
            ans.append(i*c[i])
            del c[i]
    for i in c:
        ans.append(i*c[i])
    return ("".join(ans))

 
for i in range(int(input())):
    print(sol())
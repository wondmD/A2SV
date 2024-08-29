from collections import Counter
s = input()
k = int(input())

c = Counter(s)
if len(c) < k:
    if len(c)  <= 26 and len(s) >= k:
        print(k-len(c))
    else:
        print("impossible")
else:
    print(0)
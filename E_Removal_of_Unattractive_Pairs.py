from collections import Counter
t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    

    d = Counter(s).most_common()
    md = d[0][1]
    sm = sum([i[1] for i in d[1:]])
    if 
    # print (d.values())
    
l = []
for _ in range(int(input())):
    l.append(list(map(int, input().split())))
l.sort()
def sol(x):
    tv1 = -1
    tv2 = -1
    for start, end in x:
        if tv1 < start:
            tv1 = end
        elif tv2 < start:
            tv2 = end
        else:
            return ('NO')
    return 'YES'
print(sol(l))
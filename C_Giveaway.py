stock , q = map(int, input().split())
l = list(map(int, input().split()))
l.sort()

for i in range(1, len(l)):
    l[ i] += l[i-1]

for i in range(q):
    x , y = map(int, input().split())
    diff  = len(l) - x
    if diff == 0:
        print(l[y-1])
        continue
    des = diff + y
    print(l[des-1] - l[diff-1])
from collections import deque
le,test = [int(i) for i in input().split()]
arr = [int(i) for i in input().split()]
ki = max(arr)
ind = 0
for i in range(le):
   if arr[i]==ki:
      ind = i
      break
d = deque(arr)
tops = []
for i in range(ind):
    tops.append([d[0], d[1]])
    if d[0] < d[1]:
        d.append(d.popleft())
    else:
        d[0], d[1] = d[1], d[0]
        d.append(d.popleft())
d.popleft()
for _ in range(test):
    opr = int(input())
    if opr == 0:
        break
    if opr < ind + 1:
        a = tops[opr - 1]
        print(*a)
    else:
        a = ki
        k = (opr-ind) % (len(d)) 
        b = d[k-1]
        print(*[a, b])
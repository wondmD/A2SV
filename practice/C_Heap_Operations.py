import heapq

n = int(input())

ans = []

a = "insert"
b = "removeMin"
c = "getMin"

que = []

for _ in range(n):
    s = input().split()

    if s[0] == a:
        x = int(s[1])
        heapq.heappush(que, x)
        ans.append((a, x))
    elif s[0] == b:
        if len(que) == 0:
            ans.append((a, 0))
        else:
            heapq.heappop(que)
        ans.append((b, -float('inf')))
    else:
        x = int(s[1])
        while que and que[0] < x:
            heapq.heappop(que)
            ans.append((b, -float('inf')))
        
        if len(que) == 0 or que[0] != x:
            heapq.heappush(que, x)
            ans.append((a, x))
        
        ans.append((c, x))

print(len(ans))
for op, val in ans:
    if val == -float('inf'):
        print(op)
    else:
        print(op, val)

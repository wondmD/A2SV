
from sys import stdin
from collections import defaultdict, deque
# from bisect import bisect_left, bisect_right

def sol():
    num = int(stdin.readline())
    lis = list(map(int, stdin.readline().split()))
    ans = [-1]*num
    def inb1(n, i, num):
        if n + i < num:
            return True
        return False
    def inb2(n, i):
        if i - n >= 0:
            return True
        return False
    graph = defaultdict(list)
    for i in range(num):
        if inb1(lis[i], i, num):
            graph[i].append(i +lis[i])
        if inb2(lis[i], i):
            graph[i].append(i-lis[i])
    ans = [-1]*num
    print(graph)
    for i in range(num):
        q = deque([i])
        st = 0
        p = 1 if lis[i] % 2 else 0
        visited = set()
        print(q)
        while q:
            st += 1
            leng = len(q)
            f = 0
            for i in range(leng):
                root = lis[q.popleft()]
                visited.add(root)
                for node in graph[root]:
                    if lis[node] not in visited:
                        p2 = 1 if lis[node] %2 else 0
                        if p != p2:
                            f =1
                            ans[i] = st
                            break
                        q.append(node)
            if f:
                break
    return ans

            


# for _ in range(int(input())):
print(*sol())

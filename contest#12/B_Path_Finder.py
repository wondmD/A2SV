from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

def sol():
    # pass
    num = int(stdin.readline())
    graph = defaultdict(list)

    for i in range(num-1):
        a, b,c= map(int, stdin.readline().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    

    ans = 0
    vis = set()
    def dfs(root, n):
        nonlocal ans
        ans = max(ans, n)
        vis.add(root)
        for node, dis in graph[root]:
            if node not in vis:
                dfs(node, n+dis)
        return
    dfs(0, 0)
    return ans
        


    



# for _ in range(int(input())):
print(sol())

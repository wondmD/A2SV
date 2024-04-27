# from sys import stdin
# from collections import defaultdict, deque
# from bisect import bisect_left, bisect_right

# def sol():
#     # pass
#     num = int(stdin.readline())
#     edge = list(map(int, stdin.readline().split()))
#     color = list(map(int, stdin.readline().split()))
#     graph = defaultdict(list)

#     for i in range(0,num-1):
#         graph[edge[i]].append(i+2)
#     ans = 0
#     vi = set()
#     # print(graph)
#     def dfs(root, to_col, prev):
#         nonlocal ans
#         vi.add(root)
#         if prev == to_col and prev != 0:
#             for node in graph[root]:
#                 if node not in vi:
#                     dfs(node, color[node-1], prev)
#         else:
#             ans += 1
#             # print(root)
#             for node in graph[root]:
#                 if node not in vi:
#                     dfs(node, color[node-1], color[root-1])
#     dfs(1, color[0], 0)

#     return ans

        



# # for _ in range(int(input())):
# print(sol())

import heapq, math
from itertools import *
from bisect import *
from collections import *
from sys import stdin, stdout
import sys

if "PyPy" in sys.version:
    from _continuation import continulet  # type: ignore
else:
    import threading




def solve():
    # pass
    num = int(stdin.readline())
    edge = list(map(int, stdin.readline().split()))
    color = list(map(int, stdin.readline().split()))
    graph = defaultdict(list)

    for i in range(0,num-1):
        graph[edge[i]].append(i+2)
    ans = 0
    vi = set()
    # print(graph)
    def dfs(root, to_col, prev):
        nonlocal ans
        vi.add(root)
        if prev == to_col and prev != 0:
            for node in graph[root]:
                if node not in vi:
                    dfs(node, color[node-1], prev)
        else:
            ans += 1
            # print(root)
            for node in graph[root]:
                if node not in vi:
                    dfs(node, color[node-1], color[root-1])
    dfs(1, color[0], 0)

    print(ans)


if __name__ == "__main__":
    if "PyPy" in sys.version:

        def bootstrap(cont):
            call, arg = cont.switch()
            while True:
                call, arg = cont.switch(
                    to=continulet(lambda _, f, args: f(*args), call, arg)
                )

        cont = continulet(bootstrap)
        cont.switch()

        solve()

    else:
        sys.setrecursionlimit(1 << 30)
        threading.stack_size(1 << 27)

        main_thread = threading.Thread(target=solve)
        main_thread.start()
        main_thread.join()

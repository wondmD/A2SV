#my import snippet 
from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right
import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    ans = 0
    class sol:
        def solve(self):
            ans = 0
        
            def dfs(root):
                nonlocal ans
                visited.add(root)
                leng = 1
                for node in graph[root]:
                    if node not in visited:
                        visited.add(node)
                        leng += dfs(node)
                if leng % 2 == 0:
                    ans +=1
                return leng
            num = int(stdin.readline())
            graph = defaultdict(list)
            for _ in range(num-1):
                a, b= map(int, stdin.readline().split())
                graph[a].append(b)
                graph[b].append(a)
            if num %2:
                print(-1)
            else:
                visited = set()
                dfs(1)
                print(ans-1)

    solver = sol()
    solver.solve()

if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()

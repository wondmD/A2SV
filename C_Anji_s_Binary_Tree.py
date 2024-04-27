
for test in range(int(input())):
    n = int(input())
    s = input()
    graph = {}
    for i in range(n):
        graph[i+1] = tuple(map(int, input().split()))

    stack = [(1, 0)]
    sol = n + 1

    while stack:
        v, count = stack.pop()

        if graph[v][0] != 0:
            stack.append((graph[v][0], count + (1 if s[v-1]!='L' else 0)))

        if graph[v][1] != 0:
            stack.append((graph[v][1], count + (1 if s[v-1]!='R' else 0)))

        if graph[v] == (0, 0):
            sol = min(sol, count)

    print(sol)
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    stack = []
    res = 0
    for i in l:
        if not stack or stack[-1] < i:
            stack.append(i)
        else:
            while  stack and stack[-1] > i:
                stack.pop()
                res+=1
            stack.append(i)
    print(res)
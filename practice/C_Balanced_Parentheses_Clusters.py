from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right


def find(x):
    if x == parent[x]:
        return x
    return find(parent[x])
def union(x,y):
    parent_x = find(x)
    parent_y = find(y)

    if parent_x != parent_y:
        if rank[parent_x] >= rank[parent_y]:
            parent[parent_y] = parent_x
            rank[parent_x] += 1
        else:
            parent[parent_x] = parent_y
            rank[parent_y] += 1
def valid(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
    return len(stack) == 0
for _ in range(int(input())):
    a= int(input())
    s = input()
    parent = {i:i for i in range(a*2)}
    rank = {i:1 for i in range( a*2)}

    for i in range(2*a-1):
        for j in range(i+1,2*a):
            if valid(s[i:j+1]) and s[i] == '(' and s[j] == ')':
                union(i,j)

    ans = set()
    for i in range(2*a):
        ans.add(find(i))
    print(len(ans))

    # print(valid('()'))

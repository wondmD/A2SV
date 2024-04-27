nt = int(input())
ans = []
for _ in range(nt):
    ns = int(input())
    fs = input()
    first = 0
    end = ns-1
    while first < end:
        size = len(set([fs[first],fs[end]])) 
        if  size== 2:
            ans.append(len(fs[first:end-1]))
        else:
            ans.append(len(fs[first:end])+1)
        first+=1
        end-=1

for i in ans:
    print(i)
'''
n = int(input())
for i in range(n):
    l = int(input())
    arr = list(map(int,input().split()))
'''
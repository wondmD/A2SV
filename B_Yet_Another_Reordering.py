n = int(input())
my_list= list(map(int, input().split()))
my_list.sort()


p1 = 0
p2 = 0
c = 0
while (p1 < n and p2 <n):
    if my_list[p1] < my_list[p2]:
        c+=1
        p1+=1
        p2+=1
    else:
        p2+=1
print(c)
n, k = map(int, input().split())
my_list = list(map(int, input().split()))

my_list.sort()


if (k==0 and my_list[0]>1):
    print(1)
elif k==0 and my_list[0] ==1:
    print(-1)
elif k<=n-1:
    if my_list[k-1]!=my_list[k]:
        print (my_list[k-1])
    else:
        print (-1)
elif k==n:
    print (my_list[k-1])


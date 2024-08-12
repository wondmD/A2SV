m,s=map(int,input().split())
arr=[]
if s==0 and m==1:
  print(0,0)
  exit()
elif s==0:
  print(-1 ,-1)
  exit()

else:
  while m>0:
    curr=min(s,9)
    arr.append(curr)
    s-=curr
    m-=1
if s>0:
  print(-1,-1)
  exit()
reversed_arr=arr[::-1]
j=0
while reversed_arr[j]==0:
  j+=1
reversed_arr[0]+=1
reversed_arr[j]-=1
#calculate min
minn=""
maxx=""
for i in arr:
  maxx+=str(i)
for j in reversed_arr:
  minn+=str(j)

print(minn,maxx)


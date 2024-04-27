m, n = map(int, input().split())
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
idx = 0
c = 0
for num in  nums2:
    while (idx<m and nums1[idx]< num):
        c+=1
        idx+=1
    print (c, end=" ")

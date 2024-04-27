
def sol():
    n , k = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    arr3 = []
    for i in range(n):
        arr3.append([abs(arr2[i]),arr1[i]])
    arr3.sort()
    bullet = 0 
    last = 0
 
    for axis ,live in  arr3:
        bullet += (axis- last) * k 
        
        bullet -= live
        last = axis
        if bullet < 0:
            return 'NO'
    return 'YES'

for _ in range(int(input())):
    print(sol())
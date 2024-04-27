import math

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True
num = int(input())
ans = 0
for nums in range(6,num+1):
    c = 0
    for j in range(2, nums+1):
        if nums % j == 0:
            if isPrime(j):
                c+=1
        if c > 2:
            break
    if c == 2:
        ans+=1
print(ans)
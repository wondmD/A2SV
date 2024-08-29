n = int(input())
gen = list(map(int, input().split()))
gen.sort()
print(gen[n//2])
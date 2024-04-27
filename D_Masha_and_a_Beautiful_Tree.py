def solve1(l, r, arr):
    if r - l == 1:
        return 0
    mid = (l + r) // 2
    mal = max(arr[l:mid])
    mar = max(arr[mid:r])
    ans = 0
    if mal > mar:
        ans += 1
        arr[l:mid], arr[mid:r] = arr[mid:r], arr[l:mid]
    return solve1(l, mid, arr) + solve1(mid, r, arr) + ans

def solve(arr):
    ans = solve1(0, len(arr), arr)
    if arr == sorted(arr):
        return ans
    return -1

t = int(input())
for _ in range(t):
    m = int(input())
    arr = list(map(int, input().split()))
    print(solve(arr))
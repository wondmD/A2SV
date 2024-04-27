def find_indices(arr, l, r):
    last_occurrence = {}
    for i in range(r, l - 1, -1):
        if arr[i] not in last_occurrence:
            last_occurrence[arr[i]] = i
    
    for i in range(l, r + 1):
        if last_occurrence[arr[i]] != i:
            return i, last_occurrence[arr[i]]
    return -1, -1

# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read input
    n = int(input())
    arr = list(map(int, input().split()))
    q = int(input())
    
    # Process queries
    for _ in range(q):
        l, r = map(int, input().split())
        i, j = find_indices(arr, l - 1, r - 1)
        print(i, j)
    print()  # Print an empty line after each test case

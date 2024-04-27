t = int(input())  # Number of test cases

for _ in range(t):
    n = int(input())  # Length of the array
    a = list(map(int, input().split()))  # Elements of the array

    freq = {}  # Frequency counter

    # Update frequency counter
    for num in a:
        freq[num] = freq.get(num, 0) + 1

    # Find the maximum frequency
    max_freq = max(freq.values())

    # Calculate the maximum number of elements that can be made equal
    max_elements = min(max_freq, n - max_freq)

    print(max_elements)
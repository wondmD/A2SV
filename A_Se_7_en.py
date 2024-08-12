def smallest_divisible_by_7(n):
    if n % 7 == 0:
        return n
    
    min_modification = n
    n_str = str(n)
    length = len(n_str)
    
    # Try replacing each digit from left to right
    for i in range(length):
        original_digit = n_str[i]
        for j in range(10):
            if j == int(original_digit):
                continue
            # Replace digit i with j
            modified_str = n_str[:i] + str(j) + n_str[i+1:]
            modified_num = int(modified_str)
            if modified_num % 7 == 0:
                if modified_num < min_modification:
                    min_modification = modified_num
    
    return min_modification

t = int(input())
for _ in range(t):
    n = int(input())
    result = smallest_divisible_by_7(n)
    print(result)

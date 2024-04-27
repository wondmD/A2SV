def xor_distance(a, b, r):
    # XOR operation between a and b
    xor_result = a ^ b
    
    # Find the highest bit in r
    highest_bit = 1
    while highest_bit <= r:
        highest_bit <<= 1
    
    # If the XOR result has a higher bit than r, set all lower bits to 1
    if xor_result >= highest_bit:
        xor_result |= (highest_bit - 1)
    
    # Otherwise, set the highest bit to 1
    else:
        xor_result |= highest_bit
    
    return xor_result

def solve_test_case():
    a, b, r = map(int, input().split())
    result = xor_distance(a, b, r)
    print(result)

# Input reading
t = int(input())
for _ in range(t):
    solve_test_case()

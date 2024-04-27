t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    alphabet = ''.join(chr(97 + i) for i in range(k))
    s = alphabet * n

    positions = []
    for char in reversed(alphabet):
        last_index = s.rindex(char)
        positions.append(last_index)

    result = ''
    for char in alphabet:
        result += char * n
        for position in positions:
            result = result[:position] + char + result[position:]

    print(result)
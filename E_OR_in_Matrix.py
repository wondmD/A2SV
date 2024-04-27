m, n = map(int, input().split())

# Read matrix B
B = []
for _ in range(m):
    row = list(map(int, input().split()))
    B.append(row)

A = [[0] * n for _ in range(m)]

for i in range(m):
    for j in range(n):
        if B[i][j] == 1:
            for k in range(m):
                A[k][j] = 1
            for k in range(n):
                A[i][k] = 1
def find_or_operation(matrix, i, j):
    element = matrix[i][j]
    row = matrix[i]
    row_or_result = [element | x for x in row]
    column = [matrix[x][j] for x in range(len(matrix))]
    column_or_result = [element | x for x in column]
    result = 0
    for value in row_or_result + column_or_result:
        result = result or value
    return result
is_correct = True
c = [[0] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        c[i][j] = find_or_operation(A,i,j)


# Print the result

for i in range(m):
    print(" ".join(map(str, c[i])))
if c == B:
    print("YES")
    for i in range(m):
        print(" ".join(map(str, A[i])))
else:
    print("NO")
    for i in range(m):
        print(" ".join(map(str, A[i])))
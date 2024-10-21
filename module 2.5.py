def get_matrix(n, m, value):
    matrix = []
    for row in range(n):
        matrix.append([])
    for col in range(m):
        matrix[row].append(value)

    return matrix

res1 = get_matrix(2, 2, 10)
res2 = get_matrix(3, 5, 42)
res3 = get_matrix(4, 2 ,13)

print(res1)
print(res2)
print(res3)

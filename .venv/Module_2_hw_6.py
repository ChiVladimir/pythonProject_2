def get_matrix(n, m, value):
    matrix = list()
    for i in range(0, n):
        sub_matrix = list()
        for j in range(0, m):
            sub_matrix.insert(j, value)
        matrix.append (sub_matrix)
    return matrix
a = get_matrix(2, 2, 10)
b = get_matrix(3, 5, 42)
c = get_matrix(4, 2, 13)
print(a)
print(b)
print(c)

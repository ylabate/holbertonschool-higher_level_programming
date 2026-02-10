def pascal_triangle(n):
    triangle = []
    for layer in range(1, n + 1):
        row = []
        row.append(1)
        for i in range(layer - 1, 0, -1):
            row.append(i)
        triangle.append(row)
    return triangle


for line in pascal_triangle(5):
    print(line)

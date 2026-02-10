def pascal_triangle(n):
    triangle = []
    for layer in range(1, n + 1):
        row = []
        for i in range(layer):
            if i == layer - 1 or i == 0:
                row.append(1)
            else:
                row.append(triangle[layer - 2][i - 1] + triangle[layer - 2][i])
        triangle.append(row)
    return triangle

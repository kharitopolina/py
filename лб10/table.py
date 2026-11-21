def row_sums(matrix):
    result = []
    for row in matrix:
        result.append(sum(row))
    return result
def col_sums(matrix):
    if not matrix:
        return []
    cols_count = len(matrix[0])
    result = []
    for col in range(cols_count):
        s = 0
        for row in matrix:
            s += row[col]
        result.append(s)
    return result

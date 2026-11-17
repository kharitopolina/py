def row_sums(matrix):
    if not matrix:
        return []
    return [sum(row) for row in matrix]
def column_sums(matrix):
    if not matrix or not matrix[0]:
        return []
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    col_sums = []
    for col in range(num_cols):
        current_sum = 0
        for row in range(num_rows):
            current_sum += matrix[row][col]
        col_sums.append(current_sum)
    return col_sums
def diagonal_pattern(size):
    if size < 1:
        return []
    matrix = []
    for row in range(size):
        current_row = []
        for col in range(size):
            if row == col:
                current_row.append(0)
            elif row < col:
                current_row.append(1)
            else:  # row > col
                current_row.append(2)
        matrix.append(current_row)
    return matrix
def transform(matrix):
    if not matrix:
        return []
    new_matrix = []
    for row in matrix:
        new_row = []
        for val in row:
            if val == 0:
                new_row.append(1)
            else:
                new_row.append(val)
        new_matrix.append(new_row)
    return new_matrix

from pathlib import Path
def read_matrix(path):
    file_path = Path(path)
    with open(file_path, "r", encoding="utf-8") as file:
        lines = [line.rstrip("\r\n") for line in file]
    if lines and lines[-1] == "":
        lines.pop()
    if not lines:
        raise ValueError("Строка 1: файл пустой, ожидался заголовок с размерами матрицы")
    header_parts = lines[0].split()
    if len(header_parts) != 2:
        raise ValueError("Строка 1: заголовок должен содержать два целых числа (строки и столбцы)")
    try:
        rows_count = int(header_parts[0])
        cols_count = int(header_parts[1])
    except ValueError:
        raise ValueError("Строка 1: размеры матрицы должны быть целыми числами")
    if rows_count <= 0 or cols_count <= 0:
        raise ValueError("Строка 1: количество строк и столбцов должно быть больше нуля")
    data_lines = lines[1:]
    if len(data_lines) != rows_count:
        raise ValueError(
            f"Ожидалось строк данных: {rows_count}, фактически получено: {len(data_lines)}"
        )
    matrix = []
    for idx, raw_line in enumerate(data_lines, start=2):
        if raw_line.strip() == "":
            raise ValueError(f"Строка {idx}: пустая строка внутри данных недопустима")
        parts = raw_line.split()
        if len(parts) != cols_count:
            raise ValueError(
                f"Строка {idx}: ожидалось чисел: {cols_count}, получено: {len(parts)}"
            )
        row = []
        for col_idx, token in enumerate(parts, start=1):
            try:
                value = int(token)
            except ValueError:
                raise ValueError(
                    f"Строка {idx}, элемент {col_idx}: '{token}' не является целым числом"
                )
            row.append(value)
        matrix.append(row)
    return matrix
def selected_sum(matrix):
    total = 0
    for row in matrix:
        for value in row:
            if abs(value) > 2:
                total += value
    return total
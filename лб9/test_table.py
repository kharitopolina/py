import table
def test_all():
    # 1. Тест для [[1, 2, 3], [4, 5, 6]]: суммы строк и столбцов[span_1](start_span)[span_1](end_span)
    m1 = [[1, 2, 3], [4, 5, 6]]
    assert table.row_sums(m1) == [6, 15]
    assert table.column_sums(m1) == [5, 7, 9]
    # 2. Тест для [[7]]: обе суммы и узор размера 1[span_2](start_span)[span_2](end_span)
    m2 = [[7]]
    assert table.row_sums(m2) == [7]
    assert table.column_sums(m2) == [7]
    assert table.diagonal_pattern(1) == [[0]]
    # 3. Тест для [[1], [-1], [0]]: суммы строк и столбцов[span_3](start_span)[span_3](end_span)
    m3 = [[1], [-1], [0]]
    assert table.row_sums(m3) == [1, -1, 0]
    assert table.column_sums(m3) == [0]
    # 4. Пустая матрица: суммы и преобразование возвращают [][span_4](start_span)[span_4](end_span)
    empty_m = []
    assert table.row_sums(empty_m) == []
    assert table.column_sums(empty_m) == []
    assert table.transform(empty_m) == []
    # 5. Узор размера 3 совпадает с образцом[span_5](start_span)[span_5](end_span)[span_6](start_span)[span_6](end_span)
    expected_pattern_3 = [
        [0, 1, 1],
        [2, 0, 1],
        [2, 2, 0]
    ]
    assert table.diagonal_pattern(3) == expected_pattern_3
    # 6. Проверка Варианта 6 (Нули заменить единицами) на контрольной матрице[span_7](start_span)[span_7](end_span)[span_8](start_span)[span_8](end_span)
    control_matrix = [[-2, 0, 3], [4, -5, 6]]
    expected_transformed = [[-2, 1, 3], [4, -5, 6]]
    assert table.transform(control_matrix) == expected_transformed
    # 7. Проверка независимости: изменение результата не должно портить исходную матрицу[span_9](start_span)[span_9](end_span)
    original = [[-2, 0, 3], [4, -5, 6]]
    res = table.transform(original)
    res[0][0] = 999  # меняем элемент в новой матрице
    assert original[0][0] == -2  # исходная матрица осталась неизменной
    print("Все тесты пройдены")
if __name__ == "main":
    test_all()

from pathlib import Path
from files_lab import read_matrix, selected_sum
from table import col_sums, row_sums
def read_positive_integer():
    """Повторяет ввод, пока не будет введено целое число больше нуля."""
    while True:
        user_input = input("Введите положительное целое число: ").strip()
        try:
            number = int(user_input)
        except ValueError:
            print("не целое число")
            continue
        if number <= 0:
            print("должно быть больше нуля")
            continue
        return number
def format_report(matrix):
    """Формирует текст отчёта по матрице."""
    r_sums = row_sums(matrix)
    c_sums = col_sums(matrix)
    var_result = selected_sum(matrix)
    r_text = " ".join(str(x) for x in r_sums)
    c_text = " ".join(str(x) for x in c_sums)
    return (
        f"Суммы строк: {r_text}\n"
        f"Суммы столбцов: {c_text}\n"
        f"Результат варианта: {var_result}\n"
    )
def main():
    size = read_positive_integer()
    print(f"Принято число: {size}")
    folder = Path(file).resolve().parent
    matrix_path = folder / "matrix.txt"
    report_path = folder / "report.txt"
    try:
        matrix = read_matrix(matrix_path)
        report_text = format_report(matrix)
    except FileNotFoundError:
        print(f"Ошибка: файл '{matrix_path.name}' не найден.")
        return
    except UnicodeError:
        print(f"Ошибка: неверная кодировка файла '{matrix_path.name}' (ожидается UTF-8).")
        return
    except ValueError as err:
        print(f"Ошибка формата данных: {err}")
        return
    except OSError as err:
        print(f"Ошибка доступа к файлу '{matrix_path.name}': {err}")
        return
    try:
        with open(report_path, "w", encoding="utf-8") as report_file:
            report_file.write(report_text)
    except OSError as err:
        print(f"Ошибка записи отчёта в '{report_path.name}': {err}")
        return
    print(f"Отчёт успешно сохранён в '{report_path.name}'.")
if __name__ == "main":
    main()
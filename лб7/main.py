from functions import sum_digits, average, normalize_text, select_numbers
def main():
    user_num_str = input("Введите целое число для расчета суммы цифр: ")
    try:
        user_num = int(user_num_str)
        print(f"Сумма цифр модуля числа {user_num}: {sum_digits(user_num)}")
    except ValueError:
        print("Ошибка: Введено не целое число.")
    user_list_str = input("Введите числа через пробел: ")
    if user_list_str.strip():
        num_list = [float(x) for x in user_list_str.split()]
        avg_res = average(num_list)
    else:
        num_list = []
        avg_res = average(num_list)
    if avg_res is None:
        print("Результат вычисления среднего: Нет данных")
    else:
        print(f"Среднее арифметическое: {avg_res}")
    user_text = input("Введите текст для нормализации: ")
    print(f"Нормализованный текст: '{normalize_text(user_text)}'")
    sample_list = [-5, 0, 2, 5]
    try:
        threshold_input = input("Введите порог: ")
        threshold = int(threshold_input)
        res_sample = select_numbers(sample_list, threshold)
        print(f"Результат отбора: {res_sample}")
    except ValueError:
        print("Ошибка: Порог должен быть целым числом.")
if __name__ == "__main__":
    main()

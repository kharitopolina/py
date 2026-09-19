first = "2"
second = "3"
print(f"Тип до преобразования: {type(first)}, {type(second)}")
first = int(first)
second = int(second)
print(f"Тип после преобразования: {type(first)}, {type(second)}")
print(f"Фрагмент А (Сумма): {first + second}\n")
age = input("Введите возраст: ")
print(f"Тип до преобразования: {type(age)}")
age = int(age)
print(f"Тип после преобразования: {type(age)}")
print(f"Фрагмент Б (Возраст через год): {age + 1}\n")
first = 4
second = 7
third = 10
average = (first + second + third) / 3
print(f"Фрагмент В (Среднее значение): {average}")
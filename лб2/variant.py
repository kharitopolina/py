total = int(input("Введите количество файлов: "))
capacity = int(input("Введите вместимость одного каталога: "))
full_units = total // capacity
remainder = total % capacity
total_units = ((total + capacity - 1) // capacity) * bool(total)
print(f"Полностью заполненных каталогов: {full_units}")
print(f"Остаток файлов: {remainder}")
print(f"Минимальное число каталогов: {total_units}")
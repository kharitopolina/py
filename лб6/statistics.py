
line = input('Введите строку:').strip()
if not line:
    print("Нет данных")
else:
    numbers = [int(x) for x in line.split()]
    if not numbers:
        print("Нет данных")
    else:
        count = len(numbers)
        total = sum(numbers)
        minimum = min(numbers)
        maximum = max(numbers)
        average = total / count
        print(count)
        print(total)
        print(minimum)
        print(maximum)
        print(f"{average:.2f}")

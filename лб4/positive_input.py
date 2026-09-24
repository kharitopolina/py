n = 0
while True:
    num = int(input('Введите число:'))
    if num > 0:
        break
    n+= 1
print(f"Квадрат числа: {num ** 2}")
print(f"Количество отклонённых попыток: {n}")
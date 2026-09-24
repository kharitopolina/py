n = int(input('Введите количество:'))
sum = 0
pol = 0
max = None
for i in range(n):
    num = int(input('Введите число(а):'))
    sum += num
    if num > 0:
        pol += 1
    if i == 0 or num > max:
        max = num
print(f"Сумма: {sum}")
print(f"Количество положительных: {pol}")
print(f"Максимум: {max}")
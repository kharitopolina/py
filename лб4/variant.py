n = int(input('Введите количество:'))
count = 0
total_sum = 0

for _ in range(n):
    num = int(input('Введите числа:'))
    if num % 3 == 0:
        count += 1
        total_sum += num

print(f"Количество: {count}")
print(f"Сумма: {total_sum}")
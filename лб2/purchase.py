price = int(input('Введите цену одной тетради:'))
count = int(input('Введите количество тетрадей:'))
paid = int(input('Введите переданную сумму:'))
sum = price * count
sd = paid - sum
print('Стоимость:',sum)
print('Сдача:',sd)

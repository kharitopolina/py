n = input('Введите название заказа:');
i = input('Введите имя заказчика:');
name1 = input('Введите название 1 позиции:');
col1 = int(input('Введите количество товаров 1 позиции:'));
price1 = float(input('Введите цену 1 единицы в рублях:'));
name2 = input('Введите название 2 позиции:');
col2 = int(input('Введите количество товаров 2 позиции:'));
price2 = float(input('Введите цену 2 единицы в рублях:'));
delivery = float(input('Введите стоимость доставки:'));
sum = float(input('Введите внесенную сумму:'));
disc = float(input("Введите скидку на товары (в процентах от 0 до 100): "))
st1 = col1*price1;
st2 = col2*price2;
st = st1 +st2;
disco = st * (disc/100);
stwithdisc = st - disco;
std = stwithdisc + delivery;
st0 = st + delivery;
col = col1 +col2;
cd = sum - st0;
print();
print(f"=== ЗАКАЗ: {n} ===")
print(f"Заказчик: {i}")
print("---")
print(f"{name1} | {col1} | {price1:.2f} | {st1:.2f}")
print(f"{name2} | {col2} | {price2:.2f} | {st2:.2f}")
print("---")
print(f"Стоимость товаров без доставки и скидки: {st:.2f} руб.")
print(f"Стоимость доставки: {st:.2f} руб.")
print(f"Скидка: {disc:.2f} %")
print (f"Стоимость товаров со скидкой: {stwithdisc:.2f} руб.")
print (f"Сумма со скидкой и доставкой: {std:.2f} руб.")
print(f"Общая сумма с доставкой: {st0:.2f} руб.")
print(f"Общее количество единиц: {col} шт.")
print(f"Внесено: {sum:.2f} руб.")
print(f"Сдача: {cd:.2f} руб.")

a = float(input('Введите первое число:'))
b = float(input('Введите второе число:'))
c = input('Введите одну из операций с числами:+, -, *, /')
if c == "+":
    result = a + b
    print(f"{result:.2f}")
elif c == "-":
    result = a - b
    print(f"{result:.2f}")
elif c == "*":
    result = a * b
    print(f"{result:.2f}")
elif c == "/":
    if b == 0:
        print("Деление на ноль запрещено")
    else:
        result = a / b
        print(f"{result:.2f}")
else:
    print("Неизвестная операция, попробуйте заново")
text = input("Введите строку: ")
cleaned = "".join(text.lower().split(" "))
if not cleaned:
    print("Нет текста")
elif cleaned == cleaned[::-1]:
    print("Палиндром")
else:
    print("Не палиндром")

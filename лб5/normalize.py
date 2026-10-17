text = input("Введите строку: ")
words = text.split()
norm_text = " ".join(words)

print(f"Исходная длина: {len(text)}")
print(f"Новая длина: {len(norm_text)}")
print(f"Нормализованный текст: {norm_text}")
print(f"Количество слов: {len(words)}")
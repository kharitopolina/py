text = input("Введите строку: ")
matching_words = []
for raw_word in text.split():
    cleaned_word = raw_word.strip(".,!?;:").lower()
    if not cleaned_word:
        continue
    if len(cleaned_word) == 4:
        matching_words.append(cleaned_word)
if matching_words:
    for word in matching_words:
        print(word)
    print(len(matching_words))
else:
    print("Нет совпадений")
    print(0)

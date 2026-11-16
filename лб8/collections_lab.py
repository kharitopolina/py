def word_counts(text):
    if not text or not text.strip():
        return {}
    punctuation = ".,!?;:"
    words = text.split()
    counts = {}
    for raw_word in words:
        clean_word = raw_word.strip(punctuation).lower()
        if clean_word:
            counts[clean_word] = counts.get(clean_word, 0) + 1
    return counts
def print_word_pairs(counts):
    for word in sorted(counts):
        print(f"{word}: {counts[word]}")
def common_topics(first, second):
    set1 = set(first)
    set2 = set(second)
    return sorted(list(set1 & set2))
def all_topics(first, second):
    set1 = set(first)
    set2 = set(second)
    return sorted(list(set1 | set2))
def totals_by_category(records):
    totals = {}
    for record in records:
        category = record["category"]
        hours = record["amount"]
        totals[category] = totals.get(category, 0) + hours
    return totals
def titles_in_category(records, category):
    titles = []
    for record in records:
        if record["category"] == category:
            titles.append(record["title"])
    return titles
if __name__ == "main":
    sample_text = "Python, python! SQL"
    wc = word_counts(sample_text)
    print("Словарь частот:", wc)
    print_word_pairs(wc)

    pair = ("python", wc.get("python", 0))
    name, count = pair
    print(f"Пара: {name}, {count}")

    t1 = ["python", "sql", "python"]
    t2 = ["sql", "git"]
    print("Общие темы:", common_topics(t1, t2))
    print("Все темы:", all_topics(t1, t2))

    my_records = [
        {"title": "Алгебра", "category": "лекции", "amount": 36},
        {"title": "Питон", "category": "практика", "amount": 72},
        {"title": "Физика", "category": "лекции", "amount": 36}
    ]
    print("Сумма часов по категориям:", totals_by_category(my_records))
    print("Занятия в категории 'лекции':", titles_in_category(my_records, "лекции"))

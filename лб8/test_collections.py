from collections_lab import (
    word_counts,
    common_topics,
    all_topics,
    totals_by_category,
    titles_in_category
)
if __name__ == "main":
    assert word_counts("Python, python! SQL") == {"python": 2, "sql": 1}
    assert word_counts("!!!") == {}
    assert word_counts("") == {}
    t1 = ["python", "sql", "python"]
    t2 = ["sql", "git"]
    assert common_topics(t1, t2) == ["sql"]
    assert all_topics(t1, t2) == ["git", "python", "sql"]
    assert common_topics([], ["git"]) == []
    assert all_topics([], ["git"]) == ["git"]
    records = [
        {"title": "A", "category": "основное", "amount": 4},
        {"title": "B", "category": "дополнительное", "amount": 2},
        {"title": "C", "category": "основное", "amount": 3},
    ]
    records_copy = [record.copy() for record in records]
    assert totals_by_category(records) == {"основное": 7, "дополнительное": 2}
    assert titles_in_category(records, "основное") == ["A", "C"]
    assert titles_in_category(records, "неизвестная") == []
    assert records == records_copy
    print("Все тесты успешно пройдены!")

import sys
from logic import (
    add_record,
    delete_record,
    find_records,
    set_completed,
    statistics,
    validate_records,
)
from storage import load_records, save_records
DATA_FILE = "data.json"
def print_menu():
    print("\n=== План приготовления блюд ===")
    print("1. Показать записи")
    print("2. Добавить запись")
    print("3. Найти записи")
    print("4. Изменить статус")
    print("5. Удалить запись")
    print("6. Показать статистику")
    print("7. Сохранить данные")
    print("8. Выйти")
def display_records(records: list[dict]):
    if not records:
        print("Нет записей.")
        return
    sorted_recs = sorted(records, key=lambda x: x["id"])
    for r in sorted_recs:
        status = "Блюдо приготовлено" if r["completed"] else "В процессе"
        print(
            f"ID: {r['id']} | Название: {r['title']} | Категория: {r['category']} "
            f"| Порций: {r['amount']} | Статус: {status}"
        )
def main():
    try:
        records = load_records(DATA_FILE)
        if not validate_records(records):
            print(
                "Ошибка: Файл data.json повреждён или содержит некорректную структуру."
            )
            sys.exit(1)
    except Exception as e:
        print(f"Ошибка загрузки файла: {e}")
        sys.exit(1)
    has_unsaved_changes = False
    while True:
        print_menu()
        choice = input("Выберите пункт меню (1-8): ").strip()
        if choice == "1":
            display_records(records)
        elif choice == "2":
            title = input("Введите название блюда: ").strip()
            while not title:
                print("Название не может быть пустым.")
                title = input("Введите название блюда: ").strip()
            category = input("Введите категорию (например, Супы, Десерты): ").strip()
            while not category:
                print("Категория не может быть пустой.")
                category = input("Введите категорию: ").strip()
            amount_str = input("Введите количество порций: ").strip()
            while not amount_str.isdigit() or int(amount_str) < 0:
                print("Количество порций должно быть целым неотрицательным числом.")
                amount_str = input("Введите количество порций: ").strip()

            add_record(records, title, category, int(amount_str))
            has_unsaved_changes = True
            print("Блюдо успешно добавлено в план!")
        elif choice == "3":
            query = input("Введите название блюда для поиска: ").strip()
            if not query:
                print("Поисковый запрос не может быть пустым.")
                continue
            found = find_records(records, query)
            if not found:
                print("Ничего не найдено.")
            else:
                display_records(found)
        elif choice == "4":
            rec_id_str = input("Введите ID блюда: ").strip()
            if not rec_id_str.isdigit():
                print("Некорректный ID.")
                continue
            rec_id = int(rec_id_str)
            print("Выберите новый статус:")
            print("1. Блюдо приготовлено")
            print("2. В процессе (не приготовлено)")
            st_choice = input("Ваш выбор (1/2): ").strip()
            if st_choice == "1":
                new_status = True
            elif st_choice == "2":
                new_status = False
            else:
                print("Некорректный выбор статуса.")
                continue
            if set_completed(records, rec_id, new_status):
                has_unsaved_changes = True
                print("Статус блюда успешно обновлен!")
            else:
                print("Запись с таким ID не найдена.")
        elif choice == "5":
            rec_id_str = input("Введите ID блюда для удаления: ").strip()
            if not rec_id_str.isdigit():
                print("Некорректный ID.")
                continue
            rec_id = int(rec_id_str)
            confirm = input(
                f"Вы уверены, что хотите удалить запись с ID {rec_id}? (да/нет): "
            ).strip().lower()
            if confirm == "да":
                if delete_record(records, rec_id):
                    has_unsaved_changes = True
                    print("Запись успешно удалена.")
                else:
                    print("Запись с таким ID не найдена.")
            else:
                print("Удаление отменено.")
        elif choice == "6":
            stats = statistics(records)
            print(f"\nВсего записей: {stats['total_count']}")
            print(f"Приготовлено блюд: {stats['completed_count']}")
            print(f"Осталось приготовить: {stats['uncompleted_count']}")
            print(f"Общее количество порций: {stats['total_amount']}")
            print("\nСтатистика по категориям:")
            for cat, data in stats["categories"].items():
                print(
                    f" - {cat}: блюд — {data['count']}, порций — {data['amount']}"
                )
        elif choice == "7":
            try:
                save_records(DATA_FILE, records)
                has_unsaved_changes = False
                print("Данные успешно сохранены в файл data.json!")
            except Exception as e:
                print(f"Ошибка при сохранении: {e}")
        elif choice == "8":
            while True:
                ans = input(
                    "Сохранить текущие данные перед выходом? (да/нет): "
                ).strip().lower()
                if ans == "да":
                    try:
                        save_records(DATA_FILE, records)
                        print("Данные сохранены. До свидания!")
                    except Exception as e:
                        print(f"Ошибка при сохранении: {e}")
                    sys.exit(0)
                elif ans == "нет":
                    print("Выход без сохранения. До свидания!")
                    sys.exit(0)
                else:
                    print("Пожалуйста, ответьте 'да' или 'нет'.")
        else:
            print("Некорректная команда. Попробуйте снова.")
if __name__ == "main":
    main()

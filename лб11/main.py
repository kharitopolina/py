import json
from pathlib import Path
from analysis import (
    completion_counts,
    get_leader_completed_tasks,
    select_tasks,
    top_users,
    validate_todos,
)
def read_positive_int(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print("Ошибка: введите целое число.")
            continue
        if value <= 0:
            print("Ошибка: число должно быть больше нуля.")
            continue
        return value
def save_json(path, payload):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(payload, file, ensure_ascii=False, indent=2)
def main():
    base_dir = Path(file).resolve().parent
    input_path = base_dir / "todos.json"
    leaders_path = base_dir / "leaders.json"
    selected_path = base_dir / "selected.json"
    try:
        with open(input_path, "r", encoding="utf-8") as file:
            todos = json.load(file)
        validate_todos(todos)
    except FileNotFoundError:
        print(f"Ошибка: файл '{input_path.name}' не найден.")
        return
    except UnicodeDecodeError as error:
        print(f"Ошибка кодировки файла '{input_path.name}': {error}")
        return
    except json.JSONDecodeError as error:
        print(f"Ошибка формата JSON в '{input_path.name}': {error}")
        return
    except ValueError as error:
        print(f"Ошибка структуры данных: {error}")
        return
    except OSError as error:
        print(f"Ошибка доступа к файлу: {error}")
        return
    counts = completion_counts(todos)
    leaders = top_users(counts)
    leader_tasks = get_leader_completed_tasks(todos, leaders)
    leader_task_ids = [task["id"] for task in leader_tasks]
    leaders_str = ", ".join(str(uid) for uid in leaders) if leaders else "нет"
    print(f"Количество выполненных задач по пользователям: {counts}")
    print(f"Лидеры: {leaders_str}")
    print(f"ID завершённых задач лидеров: {leader_task_ids}")
    user_id = read_positive_int("Введите положительный user_id для Варианта 6: ")
    filtered_tasks = select_tasks(todos, user_id)
    filtered_ids = [task["id"] for task in filtered_tasks]
    print(f"Отобранные задачи пользователя {user_id} (чётный id): {filtered_ids}")
    try:
        save_json(leaders_path, leader_tasks)
        save_json(selected_path, filtered_tasks)
    except OSError as error:
        print(f"Ошибка при сохранении результатов: {error}")
        return
    print("Результаты сохранены в leaders.json и selected.json.")
if __name__ == "main":
    main()
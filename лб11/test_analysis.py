import json
from pathlib import Path
from analysis import (
    completion_counts,
    get_leader_completed_tasks,
    select_tasks,
    top_users,
    validate_todos,
)
SAMPLE_TODOS = [
    {"id": 1, "userId": 5, "title": "Ввод", "completed": True},
    {"id": 2, "userId": 5, "title": "Циклы", "completed": False},
    {"id": 3, "userId": 10, "title": "Строки", "completed": True},
    {"id": 4, "userId": 10, "title": "Файлы", "completed": True},
    {"id": 5, "userId": 5, "title": "Списки", "completed": True},
]
def assert_raises_value_error(func, *args, **kwargs):
    try:
        func(*args, **kwargs)
    except ValueError:
        return
    raise AssertionError("Ожидалось исключение ValueError, но оно не возникло")
def test_sample_dataset():
    validate_todos(SAMPLE_TODOS)
    counts = completion_counts(SAMPLE_TODOS)
    assert counts == {5: 2, 10: 2}
    leaders = top_users(counts)
    assert leaders == [5, 10]
    leader_tasks = get_leader_completed_tasks(SAMPLE_TODOS, leaders)
    assert [task["id"] for task in leader_tasks] == [1, 3, 4, 5]
def test_empty_and_no_completed():
    assert completion_counts([]) == {}
    assert top_users({}) == []
    assert get_leader_completed_tasks([], []) == []
    no_done = [
        {"id": 1, "userId": 2, "title": "Задача 1", "completed": False},
        {"id": 2, "userId": 3, "title": "Задача 2", "completed": False},
    ]
    assert completion_counts(no_done) == {2: 0, 3: 0}
    assert top_users(completion_counts(no_done)) == []
    assert get_leader_completed_tasks(no_done, []) == []
def test_single_and_multiple_leaders():
    single_leader_data = [
        {"id": 1, "userId": 1, "title": "А", "completed": True},
        {"id": 2, "userId": 1, "title": "Б", "completed": True},
        {"id": 3, "userId": 2, "title": "В", "completed": True},
    ]
    assert top_users(completion_counts(single_leader_data)) == [1]
    assert top_users(completion_counts(SAMPLE_TODOS)) == [5, 10]
def test_variant_6_select_tasks():
    res_5 = select_tasks(SAMPLE_TODOS, 5)
    assert [task["id"] for task in res_5] == [2]
    assert select_tasks(SAMPLE_TODOS, 999) == []
    odd_only = [{"id": 1, "userId": 5, "title": "Нечётный", "completed": True}]
    assert select_tasks(odd_only, 5) == []
    before = json.loads(json.dumps(SAMPLE_TODOS))
    _ = select_tasks(SAMPLE_TODOS, 5)
    assert SAMPLE_TODOS == before
def test_validation_errors():
    assert_raises_value_error(validate_todos, {"id": 1})
    dup_id = [
        {"id": 1, "userId": 5, "title": "Один", "completed": True},
        {"id": 1, "userId": 6, "title": "Дубль", "completed": False},
    ]
    assert_raises_value_error(validate_todos, dup_id)
    missing_user = [{"id": 1, "title": "Без userId", "completed": True}]
    assert_raises_value_error(validate_todos, missing_user)
    bad_completed = [{"id": 1, "userId": 5, "title": "Текст", "completed": "false"}]
    assert_raises_value_error(validate_todos, bad_completed)
    bool_id = [{"id": True, "userId": 5, "title": "Bool id", "completed": True}]
    assert_raises_value_error(validate_todos, bool_id)
def test_json_roundtrip(tmp_path=None):
    target_dir = Path(tmp_path) if tmp_path is not None else Path(".")
    out_file = target_dir / "_test_selected.json"
    try:
        selected = select_tasks(SAMPLE_TODOS, 5)
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(selected, f, ensure_ascii=False, indent=2)
        with open(out_file, "r", encoding="utf-8") as f:
            loaded = json.load(f)
        validate_todos(loaded)
        assert loaded == selected
    finally:
        if out_file.exists():
            out_file.unlink()if __name__ == "main":
    test_sample_dataset()
    test_empty_and_no_completed()
    test_single_and_multiple_leaders()
    test_variant_6_select_tasks()
    test_validation_errors()
    test_json_roundtrip()
    print("Все тесты пройдены успешно!")

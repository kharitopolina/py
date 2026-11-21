import json
import os
def load_records(path: str) -> list[dict]:
    if not os.path.exists(path):
        return []

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list):
                raise ValueError("Корень JSON должен быть списком.")
            return data
    except (json.JSONDecodeError, UnicodeDecodeError) as e:
        raise ValueError(f"Ошибка чтения файла JSON: {e}")
def save_records(path: str, records: list[dict]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
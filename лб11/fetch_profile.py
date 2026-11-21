import json
import socket
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen
def fetch_profile(login):
    if not login.strip():
        raise ValueError("Логин не должен быть пустым")
    url = "https://api.github.com/users/" + quote(login.strip(), safe="")
    request = Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "python-course-lab11",
        },
    )
    with urlopen(request, timeout=10) as response:
        data = json.loads(response.read().decode("utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("login"), str):
        raise ValueError("Ответ не похож на профиль пользователя")
    return data
def print_profile_summary(data, source_label):
    print(f"[{source_label}] login: {data.get('login')}, id: {data.get('id')}, name: {data.get('name')}")
def main():
    print("Выберите источник профиля:")
    print("1 — Запрос по сети (GitHub API)")
    print("2 — Локальный пример (profile_sample.json)")
    choice = input("Ваш выбор (1/2): ").strip()
    if choice == "2":
        sample_path = Path(__file__).resolve().parent / "profile_sample.json"
        try:
            with open(sample_path, "r", encoding="utf-8") as file:
                data = json.load(file)
            print_profile_summary(data, "локальные учебные данные")
        except (OSError, json.JSONDecodeError) as error:
            print(f"Ошибка чтения локального примера: {error}")
        return
    try:
        data = fetch_profile(input("Логин GitHub: "))
        output = Path(__file__).resolve().parent / "profile.json"
        with open(output, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
        print(f"Профиль сохранён: {data['login']}")
        print_profile_summary(data, "сеть")
    except HTTPError as error:
        print(f"Сервер вернул HTTP {error.code}")
    except (URLError, TimeoutError, socket.timeout):
        print("Не удалось получить ответ по сети")
    except (ValueError, UnicodeError) as error:
        print(f"Ошибка данных: {error}")
    except OSError as error:
        print(f"Ошибка доступа: {error}")
if __name__ == "main":
    main()

# Проект вспомогательных функций Python

В этом проекте содержатся базовые математические и текстовые функции (`functions.py`), интерактивный интерфейс (`main.py`) и автоматические тесты (`test_functions.py`).

---

## Команды запуска

1. **Запуск интерактивного приложения:**
   ```bash
   python main.py
   ```

2. **Запуск автоматических тестов:**
   ```bash
   python test_functions.py
   ```

---

## Пример тестов

В проекте используются следующие `assert`-проверки для тестирования логики:

```python
from functions import sum_digits, average, normalize_text, select_numbers, is_palindrome

def run_tests():
    # Тест подсчета суммы цифр
    assert sum_digits(507) == 12
    assert sum_digits(-507) == 12

    # Тест расчета среднего арифметического
    assert average([]) is None
    assert abs(average([2, 4, 6]) - 4) < 1e-9

    # Тест проверки на палиндром
    assert is_palindrome("А роза упала на лапу Азора") is True
    assert is_palindrome("Привет") is False

if __name__ == "__main__":
    run_tests()
    print("Все тесты пройдены успешно!")
```
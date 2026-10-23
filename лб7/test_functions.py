from functions import (
    sum_digits,
    average,
    normalize_text,
    select_numbers,
    is_palindrome
)
def run_tests():
    assert sum_digits(0) == 0
    assert sum_digits(507) == 12
    assert sum_digits(-507) == 12

    assert average([]) is None
    assert abs(average([2, 4, 6]) - 4) < 1e-9

    assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
    assert normalize_text("   ") == ""
    control_list = [-5, 0, 2, 5]
    assert select_numbers(control_list, 2) == [2]
    assert select_numbers([], 2) == []
    assert select_numbers([-5, 0, 5], 2) == []
    assert select_numbers([0, 1, 3], 0) == [0]
    assert select_numbers([2, 2, 5, 2], 2) == [2, 2, 2]
    original_copy = list(control_list)
    select_numbers(control_list, 2)
    assert control_list == original_copy
    assert is_palindrome("А роза упала на лапу Азора") is True
    assert is_palindrome("Шалаш") is True
    assert is_palindrome("Привет") is False
    assert is_palindrome("   ") is False
    print("Все тесты пройдены успешно")
if __name__ == "__main__":
    run_tests()

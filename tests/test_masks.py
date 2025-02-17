import pytest

import src.masks as masks


def test_get_mask_card_number() -> None:
    """Тестирование функции get_mask_card_number(). Функция должна принимать
    номер карты в виде строки из 16 цифр в формате XXXXXXXXXXXXXXXX,
    где Х - это цифры. Если введены буквы или количество цифр меньше или
    больше 16 должна выводится ошибка ввода. При правильном вводе функция
    должна выводить номер карты в формате XXXX XX** **** XXXX"""
    assert (
        masks.get_mask_card_number("1111111111111111") == "1111 11** **** 1111"
    )
    with pytest.raises(ValueError):
        assert masks.get_mask_card_number("")
    with pytest.raises(ValueError):
        assert (
            masks.get_mask_card_number("1111")
            == "Неверный формат номера карты"
        )
    with pytest.raises(ValueError):
        assert (
            masks.get_mask_card_number("qqqqqqqqqqqqqqqq")
            == "Неверный формат номера карты"
        )


@pytest.mark.parametrize(
    "value, expected",
    [
        ("64686473678894779589", "**9589"),
        ("11111111111111111111", "**1111"),
        ("1111", "error"),
        ("", "error"),
        ("gkjfdjgdsfsfsfgfgrtr", "error"),
    ],
)
def test_get_mask_account(value: str, expected: str) -> None:
    """Тестирование функции get_mask_account(). Функция должна принимать
    номер счета в виде строки из 20 цифр в формате XXXXXXXXXXXXXXXXXXXX,
    где Х - это цифры. Если введены буквы или количество цифр меньше или
    больше 20 должна выводится ошибка ввода. При правильном вводе функция
    должна выводить номер карты в формате **XXXX"""
    if value.isdigit() and len(value) == 20:
        assert masks.get_mask_account(value) == expected
    else:
        with pytest.raises(ValueError):
            assert masks.get_mask_account(value)

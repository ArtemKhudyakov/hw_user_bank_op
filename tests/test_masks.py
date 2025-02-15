import pytest
import src.masks as masks


def test_get_mask_card_number():
    """Тестирование функции get_mask_card_number(). Функция должна принимать
    номер карты в виде строки из 16 цифр в формате XXXX XX** **** XXXX,
    где Х - это цифры. Если введены буквы или количество цифр меньше или больше 16
    должна выводится ошибка ввода """
    assert masks.get_mask_card_number(
        '1111111111111111') == '1111 11** **** 1111'
    with pytest.raises(ValueError):
        assert masks.get_mask_card_number('')
    with pytest.raises(ValueError):
        assert masks.get_mask_card_number(
            '1111') == 'Неверный формат номера карты'
    with pytest.raises(ValueError):
        assert masks.get_mask_card_number(
            'qqqqqqqqqqqqqqqq') == 'Неверный формат номера карты'


def test_get_mask_account

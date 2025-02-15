import pytest
import src.widjet as widjet

acc_and_cards_list_for_testing = [
    ("Maestro 1596837868705199", 'Maestro 1596 83** **** 5199'),
    ("Счет 64686473678894779589", 'Счет **9589'),
    ("MasterCard 7158300734726758", 'MasterCard 7158 30** **** 6758'),
    ("Счет 35383033474447895560", 'Счет **5560'),
    ("Visa Classic 6831982476737658", 'Visa Classic 6831 98** **** 7658'),
    ("Visa Platinum 8990922113665229", 'Visa Platinum 8990 92** **** 5229'),
    ("Visa Gold 5999414228426353", 'Visa Gold 5999 41** **** 6353'),
    ("Счет 73654108430135874305", 'Счет **4305'),
    ("Visa Gold 5999414228426", 'Input error'),
    ('', 'Input error'), ('73654108430135874305', '**4305'),
    ('736541084307', 'Input error'),
    ('Счет qwedsfaf', 'Input error'),
    ('Мир 1234567890876785', 'Мир 1234 56** **** 6785' )]


@pytest.mark.parametrize(
    "value, expected",
    acc_and_cards_list_for_testing)

def test_mask_account_card(value, expected):
    """Тест функции mask_account_card(). Функция принимает номер счет в формате
        "Счет 73654108430135874305" или номер карты в формате
        "MasterCard 7158300734726758" или "Visa Platinum 7000792289606361"
        и возвращет скрытый номер счета в формате "Счет **4305" или карты
        в формате "Visa Platinum 7000 79** **** 6361".
        """
    if len(value) != 0:
        if len(value.split()[-1]) == 16 or len(value.split()[-1]) == 20:
            assert widjet.mask_account_card(value) == expected
        else:
            with pytest.raises(ValueError):
                assert widjet.mask_account_card(value) == expected
    else:
        with pytest.raises(ValueError):
            assert widjet.mask_account_card(value) == expected


date_for_testing = [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ('', 'input error'),  ('Error', 'input error'),]


@pytest.mark.parametrize("value, expected", date_for_testing)

def test_get_date(value, expected):
    """Тест функции get_date(). Функция должна принимать дату в
    формате "2024-03-11T02:26:18.671407"
    и возвращать дату в формате "ДД.ММ.ГГГГ" ("11.03.2024")."""
    if value == 'Error':
        with pytest.raises(ValueError):
            assert widjet.get_date('Error')
    else:
        if len (value) > 0:
            assert widjet.get_date(value) == expected
        else:
            with pytest.raises(ValueError):
                assert widjet.get_date(value)






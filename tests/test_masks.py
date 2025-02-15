import pytest
import src.masks as masks


def test_get_mask_card_number():
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

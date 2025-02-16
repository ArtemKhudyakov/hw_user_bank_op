import pytest


@pytest.fixture
def parent_test_data() -> list[dict[str, str]]:
    return [
        {
            "id": "41428829",
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
        },
        {
            "id": "939719570",
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
        },
        {
            "id": "594226727",
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
        },
        {
            "id": "615064591",
            "state": "CANCELED",
            "date": "2018-10-14T08:21:33.419441",
        },
    ]


@pytest.fixture
def filtered_test_data_executed() -> list[dict[str, str]]:
    return [
        {
            "id": "41428829",
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
        },
        {
            "id": "939719570",
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
        },
    ]


@pytest.fixture
def filtered_test_data_canceled() -> list[dict[str, str]]:
    return [
        {
            "id": "594226727",
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
        },
        {
            "id": "615064591",
            "state": "CANCELED",
            "date": "2018-10-14T08:21:33.419441",
        },
    ]


@pytest.fixture
def sorted_by_date_data_descending() -> list[dict[str, str]]:
    return [
        {
            "id": "41428829",
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
        },
        {
            "id": "615064591",
            "state": "CANCELED",
            "date": "2018-10-14T08:21:33.419441",
        },
        {
            "id": "594226727",
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
        },
        {
            "id": "939719570",
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
        },
    ]


@pytest.fixture
def sorted_by_date_data_ascending() -> list[dict[str, str]]:
    return [
        {
            "id": "939719570",
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
        },
        {
            "id": "594226727",
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
        },
        {
            "id": "615064591",
            "state": "CANCELED",
            "date": "2018-10-14T08:21:33.419441",
        },
        {
            "id": "41428829",
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
        },
    ]

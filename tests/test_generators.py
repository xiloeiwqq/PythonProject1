from typing import Dict, List

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "transactions, currency, expected",
    [
        (
            [
                {"id": 939719570, "operationAmount": {"amount": "9824.07", "currency": {"code": "USD"}}},
                {"id": 142264268, "operationAmount": {"amount": "79114.93", "currency": {"code": "USD"}}},
                {"id": 873106923, "operationAmount": {"amount": "43318.34", "currency": {"code": "RUB"}}},
                {"id": 895315941, "operationAmount": {"amount": "56883.54", "currency": {"code": "USD"}}},
            ],
            "USD",
            [
                {"id": 939719570, "operationAmount": {"amount": "9824.07", "currency": {"code": "USD"}}},
                {"id": 142264268, "operationAmount": {"amount": "79114.93", "currency": {"code": "USD"}}},
                {"id": 895315941, "operationAmount": {"amount": "56883.54", "currency": {"code": "USD"}}},
            ],
        ),
        (
            [
                {"id": 873106923, "operationAmount": {"amount": "43318.34", "currency": {"code": "RUB"}}},
                {"id": 594226727, "operationAmount": {"amount": "67314.70", "currency": {"code": "RUB"}}},
            ],
            "USD",
            [],
        ),
    ],
)
def test_filter_by_currency(transactions: List[Dict], currency: str, expected: List[Dict]):
    assert list(filter_by_currency(transactions, currency)) == expected


def filter_by_currency(transactions, currency):
    return [t for t in transactions if t["operationAmount"]["currency"]["code"] == currency]


@pytest.mark.parametrize(
    "transactions, expected",
    [
        (
            [
                {"id": 939719570, "operationAmount": {"amount": "9824.07", "currency": {"code": "USD"}}},
                {"id": 142264268, "operationAmount": {"amount": "79114.93", "currency": {"code": "USD"}}},
            ],
            ["Transaction 939719570: 9824.07 USD", "Transaction 142264268: 79114.93 USD"],
        ),
        ([], []),
    ],
)
def test_transaction_descriptions(transactions: List[Dict], expected: List[str]):
    assert list(transaction_descriptions(transactions)) == expected


@pytest.fixture
def card_generator():
    start = 0
    stop = 10
    return card_number_generator(start, stop + 1)


def test_card_number_generator(card_generator):
    first_number = next(card_generator)
    assert len(first_number) == 19
    assert first_number[:4] == "0000"


"""проверка всех функций модуля generators"""

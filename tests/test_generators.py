import pytest
from typing import List, Dict
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.mark.parametrize(
    "transactions, currency, expected",
    [
        (
            [
                {"index": 1, "amount": 900, "currency": "USD"},
                {"index": 2, "amount": 400, "currency": "EUR"},
                {"index": 3, "amount": 150, "currency": "USD"},
                {"index": 4, "amount": 1400, "currency": "RUB"},
            ],
            "USD",
            [{"index": 1, "amount": 900, "currency": "USD"}, {"index": 3, "amount": 150, "currency": "USD"}],
        ),
        ([{"index": 1, "amount": 900, "currency": "USD"}, {"index": 3, "amount": 150, "currency": "USD"}], "EUR", []),
    ],
)
def test_filter_by_currency(transactions: List[Dict], currency: str, expected: List[Dict]):
    assert list(filter_by_currency(transactions, currency)) == expected


@pytest.mark.parametrize(
    "transactions, expected",
    [
        (
            [{"index": 1, "amount": 900, "currency": "USD"}, {"index": 2, "amount": 400, "currency": "EUR"}],
            ["Transaction 1: 900 USD", "Transaction 2: 400 EUR"],
        ),
        ([], []),
    ],
)
def test_transaction_descriptions(transactions: List[Dict], expected: List[str]):
    assert list(transaction_descriptions(transactions)) == expected


@pytest.fixture
def card_generator():
    return card_number_generator()


def test_card_number_generator(card_generator):
    first_number = next(card_generator)
    assert len(first_number) == 19
    assert first_number[:4] == "0000"

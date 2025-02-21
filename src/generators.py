from typing import List, Dict, Iterator


def filter_by_currency(transactions: List[Dict], currency: str) -> Iterator[Dict]:
    return (transaction for transaction in transactions if transaction.get("currency") == currency)


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    return (f"Transaction {t['index']}: {t['amount']} {t['currency']}" for t in transactions)


def card_number_generator() -> Iterator[str]:
    for number in range(1, 10**16):
        yield (
            f"{number:016}"[:4] + " " + f"{number:016}"[4:8] + " " + f"{number:016}"[8:12] + " " + f"{number:016}"[12:]
        )


transactions = [
    {"index": 1, "amount": 900, "currency": "USD"},
    {"index": 2, "amount": 400, "currency": "EUR"},
    {"index": 3, "amount": 150, "currency": "USD"},
    {"index": 4, "amount": 1400, "currency": "RUB"},
]


filtered_transactions = filter_by_currency(transactions, "USD")
for transaction in filtered_transactions:
    print(transaction)

descriptions = transaction_descriptions(transactions)
for description in descriptions:
    print(description)


generator = card_number_generator()
for _ in range(5):
    print(next(generator))

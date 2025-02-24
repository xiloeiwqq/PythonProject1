from typing import List, Dict, Iterator


def filter_by_currency(transactions: List[Dict], currency: str) -> Iterator[Dict]:
    return (transaction for transaction in transactions if transaction.get("currency_code") == currency)


"""принимает на вход список словарей, представляющих транзакции"""


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    return (f"Transaction {t['index']}: {t['amount']} {t['currency']}" for t in transactions)


"""принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""


def card_number_generator(start: int, stop:int) -> Iterator[str]:
    for number in range(start, stop+1):
        yield (
            f"{number:016}"[:4] + " " + f"{number:016}"[4:8] + " " + f"{number:016}"[8:12] + " " + f"{number:016}"[12:]
        )


"""выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""


transactions = [
    {"index": 1, "amount": 900, "currency": "USD"},
    {"index": 2, "amount": 400, "currency": "EUR"},
    {"index": 3, "amount": 150, "currency": "USD"},
    {"index": 4, "amount": 1400, "currency": "RUB"}
]


import json
import csv
import pandas as pd
import re


# Функции для загрузки данных
def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


def load_csv(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return list(csv.DictReader(file))


def load_xlsx(filename):
    df = pd.read_excel(filename)
    return df.to_dict(orient='records')


# Функции фильтрации
def search_transactions(transactions, search_str):
    pattern = re.compile(search_str, re.IGNORECASE)
    return [transaction for transaction in transactions if pattern.search(transaction.get('description', ''))]


def filter_by_status(transactions, status):
    status = status.lower()  # Приводим статус к нижнему регистру для корректной работы
    return [transaction for transaction in transactions if transaction.get('status', '').lower() == status]


def count_by_category(transactions, categories):
    category_counts = {category: 0 for category in categories}
    for transaction in transactions:
        description = transaction.get('description', '').lower()
        for category in categories:
            if category.lower() in description:
                category_counts[category] += 1
    return category_counts


def main():
    print("приветик! добро пожаловать в программу работы с банковскими транзакциями.")
    print("выберите необходимый пункт меню:")
    print("1. получить информацию о транзакциях из JSON-файла")
    print("2. получить информацию о транзакциях из CSV-файла")
    print("3. получить информацию о транзакциях из XLSX-файла")

    file_choice = input("ваш выбор: ")
    if file_choice == '1':
        filename = input("введите имя JSON-файла: ")
        transactions = load_json(filename)
    elif file_choice == '2':
        filename = input("введите имя CSV-файла: ")
        transactions = load_csv(filename)
    elif file_choice == '3':
        filename = input("введите имя XLSX-файла: ")
        transactions = load_xlsx(filename)
    else:
        print("неверный выбор.")
        return

    print(f"для обработки выбраны транзакции из файла: {filename}")

    valid_statuses = ['executed', 'canceled', 'pending']
    while True:
        status = input(
            "введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING: ")
        if status.lower() in valid_statuses:
            break
        else:
            print(f"статус операции '{status}' недоступен.")

    filtered_transactions = filter_by_status(transactions, status)

    print(f"операции отфильтрованы по статусу: {status.upper()}")

    sort_choice = input("отсортировать операции по дате? Да/Нет: ").strip().lower()
    if sort_choice == 'да':
        sort_order = input("отсортировать по возрастанию или по убыванию? ").strip().lower()
        reverse = sort_order == 'по убыванию'
        filtered_transactions.sort(key=lambda x: x.get('date', ''), reverse=reverse)

    currency_choice = input("выводить только рублевые транзакции? Да/Нет: ").strip().lower()
    if currency_choice == 'да':
        filtered_transactions = [transaction for transaction in filtered_transactions if
                                 'RUB' in transaction.get('amount', '')]

    search_choice = input("отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").strip().lower()
    if search_choice == 'да':
        search_str = input("введите слово для поиска в описаниях: ")
        filtered_transactions = search_transactions(filtered_transactions, search_str)

    if filtered_transactions:
        print("распечатываю итоговый список транзакций...")
        print(f"всего банковских операций в выборке: {len(filtered_transactions)}")
        for transaction in filtered_transactions:
            print(f"{transaction.get('date')} {transaction.get('description')}")
            print(f"Сумма: {transaction.get('amount')}")
    else:
        print("не найдено ни одной транзакции, подходящей под фильтры")


main()
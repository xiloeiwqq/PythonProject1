import csv
import pandas as pd
import os


def read_transactions_from_csv(file_path_csv):
    """считывает операции из .csv-файла."""
    transactions = []

    if not os.path.exists(file_path_csv):
        print(f"ошибка: файл '{file_path_csv}' не найден.")
        return transactions

    try:
        with open(file_path_csv, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                transactions.append(row)
    except Exception as e:
        print(f"ошибка при чтении csv-файла: {e}")

    return transactions


def read_transactions_from_excel(file_path_xlsx):
    """считывает операции из .xlsx-файла"""
    transactions = []

    if not os.path.exists(file_path_xlsx):
        print(f"ошибка: файл '{file_path_xlsx}' не найден.")
        return transactions

    try:
        df = pd.read_excel(file_path_xlsx)
        transactions = df.to_dict(orient='records')
    except Exception as e:
        print(f"Ошибка при чтении xlsx-файла: {e}")

    return transactions


print("текущая рабочая директория:", os.getcwd())


csv_path = os.path.abspath('transactions.csv')
excel_path = os.path.abspath('transactions_excel.xlsx')


read_transactions_from_csv(csv_path)
read_transactions_from_excel(excel_path)
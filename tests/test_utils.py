import json
import os
import unittest
from unittest import mock

from src.utils import load_transactions


class TestLoadTransactions(unittest.TestCase):


    @mock.patch("os.path.exists")
    @mock.patch("builtins.open")
    @mock.patch("json.load")
    def test_load_transactions_success(self, mock_json_load, mock_open, mock_exists):
        """проверяет успешное чтение транзакций из JSON-файла"""
        mock_exists.return_value = True
        mock_open.return_value.__enter__.return_value = mock.Mock()
        mock_open.return_value.__enter__.return_value.read.return_value = '[{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]'
        mock_json_load.return_value = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]

        transactions = load_transactions("transactions.json")

        self.assertEqual(transactions, [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}])
        mock_exists.assert_called_once_with("transactions.json")
        mock_open.assert_called_once_with("transactions.json", "r", encoding="utf-8")
        mock_json_load.assert_called_once()


    @mock.patch("os.path.exists")
    def test_load_transactions_file_not_exists(self, mock_exists):
        """проверяет, что возвращается пустой список, если файл не найден"""
        mock_exists.return_value = False

        transactions = load_transactions("non_existent_file.json")
        self.assertEqual(transactions, [])
        mock_exists.assert_called_once_with("non_existent_file.json")


    @mock.patch("os.path.exists")
    @mock.patch("builtins.open")
    @mock.patch("json.load")
    def test_load_transactions_invalid_json(self, mock_json_load, mock_open, mock_exists):
        """проверяет, что возвращается пустой список при ошибке в JSON"""
        mock_exists.return_value = True
        mock_open.return_value.__enter__.return_value = mock.Mock()
        mock_json_load.side_effect = json.JSONDecodeError("Expecting value", "", 0)

        transactions = load_transactions("invalid_json_file.json")
        self.assertEqual(transactions, [])
        mock_exists.assert_called_once_with("invalid_json_file.json")
        mock_open.assert_called_once_with("invalid_json_file.json", "r", encoding="utf-8")
        mock_json_load.assert_called_once()


    @mock.patch("os.path.exists")
    @mock.patch("builtins.open")
    def test_load_transactions_not_a_list(self, mock_open, mock_exists):
        """проверяет, что возвращается пустой список, если в файле не список"""
        mock_exists.return_value = True
        mock_open.return_value.__enter__.return_value = mock.Mock()
        mock_open.return_value.__enter__.return_value.read.return_value = '{"id": 1, "amount": 100}'

        transactions = load_transactions("not_a_list_file.json")
        self.assertEqual(transactions, [])
        mock_exists.assert_called_once_with("not_a_list_file.json")
        mock_open.assert_called_once_with("not_a_list_file.json", "r", encoding="utf-8")


    @mock.patch("os.path.exists")
    def test_load_transactions_io_error(self, mock_exists):
        """проверяет, что возвращается пустой список при ошибке ввода-вывода"""
        mock_exists.return_value = True

        with mock.patch("builtins.open", side_effect=IOError):
            transactions = load_transactions("file_with_io_error.json")
            self.assertEqual(transactions, [])


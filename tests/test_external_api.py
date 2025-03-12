import os
import unittest
from unittest.mock import Mock, patch

from src.external_api import convert_to_rub, process_transaction  # Заменили на внешний модуль external_api


class TestCurrencyConverter(unittest.TestCase):


    @patch("requests.get")
    def test_convert_to_rub_usd(self, mock_get):
        # Мокаем ответ от API
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'result': 75.5}
        mock_get.return_value = mock_response

        # Тестируем конвертацию из USD в рубли
        result = convert_to_rub(10, "USD")
        self.assertEqual(result, 75.5)
        mock_get.assert_called_once_with(
            "https://api.apilayer.com/exchangerates_data/convert",
            params={"from": "USD", "to": "RUB", "amount": 10},
        headers={"apikey": API_KEY}  # Замените на ваш ключ или мокируйте это
        )


    @patch("requests.get")
    def test_convert_to_rub_eur(self, mock_get):
        # Мокаем ответ от API
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'result': 85.0}  # предполагаемая конвертация в рубли
        mock_get.return_value = mock_response

        # Тестируем конвертацию из EUR в рубли
        result = convert_to_rub(10, "EUR")
        self.assertEqual(result, 85.0)


    def test_convert_to_rub_invalid_currency(self):
        # Тест на валюту, которая не поддерживается
        with self.assertRaises(ValueError):
            convert_to_rub(10, "GBP")


    @patch("requests.get")
    def test_convert_to_rub_api_error(self, mock_get):
        # Мокаем ошибку от API (например, 500 ошибка)
        mock_response = Mock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        # Тестируем ошибку API
        with self.assertRaises(Exception) as context:
            convert_to_rub(10, "USD")
        self.assertTrue("ошибка при обращении к API" in str(context.exception))


    def test_process_transaction_usd(self):
        # Тестируем обработку транзакции с USD
        transaction = {'amount': 100, 'currency': 'USD'}
        with patch("requests.get") as mock_get:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {'result': 75.5}  # ожидаемая сумма в рублях
            mock_get.return_value = mock_response

            result = process_transaction(transaction)
            self.assertEqual(result, 75.5)


    def test_process_transaction_eur(self):
        # Тестируем обработку транзакции с EUR
        transaction = {'amount': 100, 'currency': 'EUR'}
        with patch("requests.get") as mock_get:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {'result': 85.0}  # ожидаемая сумма в рублях
            mock_get.return_value = mock_response

            result = process_transaction(transaction)
            self.assertEqual(result, 85.0)


    def test_process_transaction_rub(self):
        # Тестируем обработку транзакции с RUB (не нуждается в конвертации)
        transaction = {'amount': 100, 'currency': 'RUB'}
        result = process_transaction(transaction)
        self.assertEqual(result, 100)


    def test_process_transaction_invalid_currency(self):
        # Тестируем обработку транзакции с валютой, которая не поддерживается
        transaction = {'amount': 100, 'currency': 'GBP'}
        with self.assertRaises(ValueError):
            process_transaction(transaction)


API_KEY = os.getenv("API_KEY")
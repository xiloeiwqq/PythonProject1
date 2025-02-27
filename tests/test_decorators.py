import os
import pytest
from src.decorators import log, my_function, error_function


def setup_function():
    """oчищает логи перед каждым тестом."""
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")


def test_successful_function():
    setup_function()
    logged_func = log("test_log.txt")(my_function)
    result = logged_func(3, 4)
    assert result == 7
    with open("test_log.txt", "r", encoding="utf-8") as f:
        log_content = f.read().strip()
    assert log_content == "my_function ok"


def test_function_with_error():
    setup_function()
    """очистка файла перед тестом"""
    logged_func = log("test_log.txt")(error_function)
    result = logged_func(0)
    assert result is None
    with open("test_log.txt", "r", encoding="utf-8") as f:
        log_content = f.read().strip()
    print("Log content:", log_content)
    assert "error_function ok" in log_content

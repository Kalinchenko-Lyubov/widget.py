import os
from datetime import time

import pytest

from src.decorators import log


@pytest.fixture
def temp_log_file():
    """Фикстура: создаёт временный файл для логов и удаляет его после теста."""
    filename = "test_log.txt"
    yield filename
    if os.path.exists(filename):
        os.remove(filename)


def test_success_file_output(temp_log_file):
    """Тестируем успешное выполнение — логи в файл."""

    @log(filename=temp_log_file)
    def add(a, b):
        return a + b

    result = add(3, 4)
    assert result == 7

    with open(temp_log_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    assert len(lines) == 1
    line = lines[0].strip()

    timestamp_str = line[:19]
    time.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")  # проверка формата

    assert "add (3, 4), {} ok at" in line
    assert "Result: 7" in line


def test_error_file_output(temp_log_file):
    """Тестируем ошибку — логи в файл."""

    @log(filename=temp_log_file)
    def div(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        div(1, 0)

    with open(temp_log_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    assert len(lines) == 1
    line = lines[0].strip()

    timestamp_str = line[:19]
    time.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")

    assert "div error: ZeroDivisionError at" in line
    assert "Inputs: (1, 0), {}" in line


def test_success_console_output(capsys):
    """Тестируем успешный вывод в консоль"""

    @log()
    def greet(name):
        return f"Hello, {name}!"

    result = greet("Alice")
    assert result == "Hello, Alice!"

    captured = capsys.readouterr()
    output = captured.out.strip()

    timestamp_str = output[:19]
    time.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")

    assert "greet ('Alice',), {} ok at" in output
    assert "Result: Hello, Alice!" in output


def test_error_console_output(capsys):
    """Тестируем ошибку — вывод в консоль"""

    @log()
    def risky_func(n):
        if n < 0:
            raise ValueError("Negative value")
        return n**0.5

    with pytest.raises(ValueError, match="Negative value"):
        risky_func(-1)

    captured = capsys.readouterr()
    output = captured.out.strip()

    timestamp_str = output[:19]
    time.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")

    assert "risky_func error: ValueError at" in output
    assert "Inputs: (-1,), {}" in output

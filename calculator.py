"""Простой модуль калькулятора.

Поддерживает базовые арифметические операции: сложение, вычитание,
умножение и деление. Модуль можно использовать как библиотеку и запускать
как скрипт командной строки.
"""

from __future__ import annotations

import argparse
from typing import Callable, Dict

Number = float


def add(a: Number, b: Number) -> Number:
    """Возвращает сумму двух чисел."""
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Возвращает разность двух чисел."""
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Возвращает произведение двух чисел."""
    return a * b


def divide(a: Number, b: Number) -> Number:
    """Возвращает частное от деления ``a`` на ``b``.

    Поднимает ``ZeroDivisionError``, если ``b`` равно нулю.
    """
    if b == 0:
        raise ZeroDivisionError("Деление на ноль недопустимо")
    return a / b


OPERATIONS: Dict[str, Callable[[Number, Number], Number]] = {
    "add": add,
    "sub": subtract,
    "mul": multiply,
    "div": divide,
}


def calculate(a: Number, b: Number, operation: str) -> Number:
    """Выполняет арифметическую операцию над числами ``a`` и ``b``."""
    try:
        func = OPERATIONS[operation]
    except KeyError as exc:
        raise ValueError(
            f"Неизвестная операция '{operation}'. Доступны: {', '.join(OPERATIONS)}"
        ) from exc
    return func(a, b)


def parse_args(args: list[str] | None = None) -> argparse.Namespace:
    """Парсит аргументы командной строки."""
    parser = argparse.ArgumentParser(description="Базовый калькулятор")
    parser.add_argument("a", type=float, help="Первое число")
    parser.add_argument("b", type=float, help="Второе число")
    parser.add_argument(
        "operation",
        choices=tuple(OPERATIONS.keys()),
        help="Операция: add, sub, mul или div",
    )
    return parser.parse_args(args)


def main(argv: list[str] | None = None) -> None:
    """Точка входа для запуска из командной строки."""
    args = parse_args(argv)
    result = calculate(args.a, args.b, args.operation)
    print(result)


if __name__ == "__main__":
    main()

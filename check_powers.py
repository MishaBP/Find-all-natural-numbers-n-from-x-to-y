"""Проверка чисел из диапазона: равно ли n**degree произведению его делителей.

Запуск: python check_powers.py
Ввод (по одному числу в строке): от, до, желаемая степень.
"""

from __future__ import annotations

import argparse
import sys

from analyzer import analyze
from dividers import product_of_divisors


def read_int(prompt: str) -> int:
    try:
        return int(input(prompt))
    except ValueError:
        sys.exit(f"Ошибка: ожидалось целое число, получено: {prompt.strip(': ')}")


def check_powers(x_from: int, x_to: int, degree: int) -> list[int]:
    """Числа из [x_from; x_to], для которых n**degree == произведение делителей n."""
    if x_from > x_to:
        x_from, x_to = x_to, x_from
    if x_from < 1:
        raise ValueError("диапазон должен начинаться с натурального числа (>= 1)")
    found: list[int] = []
    for i in range(x_from, x_to + 1):
        if i**degree == product_of_divisors(i):
            print(f"{i=}, {i}^{degree}={i ** degree}")
            found.append(i)
    return found


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description="Проверка степеней и анализ чисел из диапазона."
    )
    parser.add_argument("--from", dest="x_from", type=int, help="начало диапазона")
    parser.add_argument("--to", dest="x_to", type=int, help="конец диапазона")
    parser.add_argument("--degree", type=int, help="желаемая степень")
    parser.add_argument(
        "--analyze",
        action="store_true",
        help="после проверки вывести классификацию каждого числа диапазона",
    )
    args = parser.parse_args(argv)

    if args.x_from is not None and args.x_to is not None and args.degree is not None:
        x_from, x_to, degree = args.x_from, args.x_to, args.degree
    else:
        x_from = read_int("От: ")
        x_to = read_int("До: ")
        degree = read_int("Степень: ")

    try:
        check_powers(x_from, x_to, degree)
    except ValueError as exc:
        sys.exit(f"Ошибка: {exc}")

    if args.analyze:
        start = min(x_from, x_to)
        stop = max(x_from, x_to)
        print("\n--- Классификация ---")
        for i in range(start, stop + 1):
            p = analyze(i)
            print(f"{i}: {p.classify()}, делителей={p.divisor_count}, сумма делителей={p.divisor_sum}")


if __name__ == "__main__":
    main()

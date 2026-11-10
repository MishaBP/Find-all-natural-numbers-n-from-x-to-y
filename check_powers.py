"""Проверка чисел из диапазона: равно ли n**degree произведению его делителей.

Запуск: python check_powers.py
Ввод (по одному числу в строке): от, до, желаемая степень.
"""

from __future__ import annotations

import math
import sys

from dividers import get_divisors


def read_int(prompt: str) -> int:
    try:
        return int(input(prompt))
    except ValueError:
        sys.exit(f"Ошибка: ожидалось целое число, получено: {prompt.strip(': ')}")


def main() -> None:
    x_from = read_int("От: ")
    x_to = read_int("До: ")
    degree = read_int("Степень: ")

    if x_from > x_to:
        x_from, x_to = x_to, x_from
    if x_from < 1:
        sys.exit("Ошибка: диапазон должен начинаться с натурального числа (>= 1).")

    for i in range(x_from, x_to + 1):
        divisors = get_divisors(i)
        if i ** degree == math.prod(divisors):
            print(f"{i=}, {i}^{degree}={i ** degree}, делители={divisors}")


if __name__ == "__main__":
    main()

"""Анализ натуральных чисел: характеристики, поиск «интересных» чисел.

Использует dividers.get_divisors и number_theory.is_prime.
"""

from __future__ import annotations

from dataclasses import dataclass

from dividers import get_divisors, sum_of_divisors
from number_theory import is_prime


@dataclass(frozen=True)
class NumberProfile:
    """Набор характеристик одного натурального числа."""

    n: int
    divisors: list[int]
    divisor_count: int
    divisor_sum: int
    is_perfect: bool
    is_deficient: bool
    is_abundant: bool
    prime: bool

    def classify(self) -> str:
        if self.prime:
            return "простое"
        if self.n == 1:
            return "единица"
        if self.is_perfect:
            return "совершенное"
        return "избыточное" if self.is_abundant else "недостаточное"


def analyze(n: int) -> NumberProfile:
    """Возвращает полный профиль числа n (делители, сумма делителей, тип)."""
    if n <= 0:
        raise ValueError(f"n должно быть натуральным числом, получено: {n}")
    divisors = get_divisors(n)
    proper_sum = sum_of_divisors(n) - n
    return NumberProfile(
        n=n,
        divisors=divisors,
        divisor_count=len(divisors),
        divisor_sum=sum_of_divisors(n),
        is_perfect=proper_sum == n and n > 1,
        is_deficient=proper_sum < n,
        is_abundant=proper_sum > n,
        prime=is_prime(n),
    )


def perfect_numbers_in_range(x_from: int, x_to: int) -> list[int]:
    """Все совершенные числа в диапазоне [x_from; x_to]."""
    if x_from > x_to:
        x_from, x_to = x_to, x_from
    if x_from < 1:
        raise ValueError("диапазон должен начинаться с натурального числа (>= 1)")
    return [
        n
        for n in range(max(x_from, 2), x_to + 1)
        if sum_of_divisors(n) - n == n
    ]


def abundant_numbers_in_range(x_from: int, x_to: int) -> list[int]:
    """Все избыточные числа в диапазоне [x_from; x_to]."""
    if x_from > x_to:
        x_from, x_to = x_to, x_from
    if x_from < 1:
        raise ValueError("диапазон должен начинаться с натурального числа (>= 1)")
    return [n for n in range(x_from, x_to + 1) if sum_of_divisors(n) - n > n]

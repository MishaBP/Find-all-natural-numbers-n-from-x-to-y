"""Утилиты для работы с делителями и простыми множителями."""

from __future__ import annotations


def get_divisors(n: int) -> list[int]:
    """Возвращает все натуральные делители числа n по возрастанию.

    Работает за O(sqrt(n)): перебираем кандидаты до корня,
    каждый делитель i добавляем вместе с парным n // i.
    """
    if n <= 0:
        raise ValueError(f"n должно быть натуральным числом, получено: {n}")

    small: list[int] = []
    large: list[int] = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            small.append(i)
            if i != n // i:
                large.append(n // i)
        i += 1
    return small + large[::-1]


def prime_factorization(n: int) -> list[int]:
    """Возвращает список простых множителей числа n (с повторами).

    Например: 12 -> [2, 2, 3].
    """
    if n < 2:
        return []

    factors: list[int] = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

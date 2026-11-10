"""Утилиты для работы с делителями и простыми множителями."""

from __future__ import annotations

import math


def divisor_count(n: int) -> int:
    """Количество натуральных делителей числа n (tau-функция), за O(sqrt(n))."""
    if n <= 0:
        raise ValueError(f"n должно быть натуральным числом, получено: {n}")

    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
        i += 1
    return count


def is_perfect(n: int) -> bool:
    """Совершенное ли число: сумма собственных делителей равна самому числу."""
    if n <= 0:
        raise ValueError(f"n должно быть натуральным числом, получено: {n}")
    return sum_of_divisors(n) == 2 * n


def product_of_divisors(n: int) -> int:
    """Произведение всех натуральных делителей числа n.

    По формуле: произведение = n^(tau(n)/2). Реализовано полностью в целых
    числах: если tau чётное — n^(tau//2); иначе n — точный квадрат и ответ
    (√n)^tau.
    """
    if n <= 0:
        raise ValueError(f"n должно быть натуральным числом, получено: {n}")
    tau = divisor_count(n)
    if tau % 2 == 0:
        return n ** (tau // 2)
    root = math.isqrt(n)  # нечётное tau гарантированно означает точный квадрат
    return root**tau


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


def sum_of_divisors(n: int) -> int:
    """Сумма всех натуральных делителей числа n (сигма-функция), за O(sqrt(n))."""
    if n <= 0:
        raise ValueError(f"n должно быть натуральным числом, получено: {n}")

    total = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            total += i
            other = n // i
            if other != i:
                total += other
        i += 1
    return total


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

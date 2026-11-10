"""Новые числовые функции: НОД, НОК, решето Эратосфена, числа Фибоначчи.

Все функции работают за приемлемое время и покрыты тестами в test_number_theory.py.
"""

from __future__ import annotations

import math


def gcd(a: int, b: int) -> int:
    """Наибольший общий делитель двух целых чисел (алгоритм Евклида).

    Результат всегда неотрицателен; gcd(0, 0) == 0.
    """
    return math.gcd(a, b)


def lcm(a: int, b: int) -> int:
    """Наименьшее общее кратное двух целых чисел.

    lcm(a, 0) == 0 по соглашению.
    """
    if a == 0 or b == 0:
        return 0
    return abs(a // gcd(a, b) * b)


def gcd_many(*numbers: int) -> int:
    """НОД произвольного количества целых чисел."""
    if not numbers:
        raise ValueError("нужно хотя бы одно число")
    result = 0
    for n in numbers:
        result = gcd(result, n)
    return result


def lcm_many(*numbers: int) -> int:
    """НОК произвольного количества целых чисел."""
    if not numbers:
        raise ValueError("нужно хотя бы одно число")
    result = 1
    for n in numbers:
        result = lcm(result, n)
    return result


def is_prime(n: int) -> bool:
    """Проверка простоты числа за O(sqrt(n))."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def sieve_of_eratosthenes(limit: int) -> list[int]:
    """Возвращает все простые числа <= limit (решето Эратосфена).

    Работает за O(n log log n). При limit < 2 возвращает пустой список.
    """
    if limit < 2:
        return []
    is_p = bytearray(b"\x01") * (limit + 1)
    is_p[0] = is_p[1] = 0
    for i in range(2, int(limit**0.5) + 1):
        if is_p[i]:
            is_p[i * i :: i] = bytearray(len(is_p[i * i :: i]))
    return [i for i, flag in enumerate(is_p) if flag]


def fibonacci(n: int) -> int:
    """n-е число Фибоначчи (F0 = 0, F1 = 1), итеративно, за O(n).

    Принимает только n >= 0.
    """
    if n < 0:
        raise ValueError(f"n должно быть >= 0, получено: {n}")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fibonacci_list(count: int) -> list[int]:
    """Первые `count` чисел Фибоначчи: [F0, F1, ..., F(count-1)]."""
    if count < 0:
        raise ValueError(f"count должно быть >= 0, получено: {count}")
    result: list[int] = []
    a, b = 0, 1
    for _ in range(count):
        result.append(a)
        a, b = b, a + b
    return result

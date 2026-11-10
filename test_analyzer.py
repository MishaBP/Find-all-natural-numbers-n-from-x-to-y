"""Тесты для analyzer.py и новых функций dividers.sum_of_divisors."""

import random

from analyzer import abundant_numbers_in_range, analyze, perfect_numbers_in_range
from dividers import get_divisors, sum_of_divisors


def brute_force_sigma(n: int) -> int:
    return sum(d for d in range(1, n + 1) if n % d == 0)


def test_sum_of_divisors_known_values():
    assert sum_of_divisors(1) == 1
    assert sum_of_divisors(6) == 12  # 1+2+3+6
    assert sum_of_divisors(12) == 28  # 1+2+3+4+6+12
    assert sum_of_divisors(97) == 98  # простое: 1 + 97


def test_sum_of_divisors_matches_brute_force():
    rng = random.Random(123)
    for _ in range(200):
        n = rng.randint(1, 5000)
        assert sum_of_divisors(n) == brute_force_sigma(n), f"n={n}"
        assert sum_of_divisors(n) == sum(get_divisors(n)), f"n={n}"


def test_sum_of_divisors_invalid_input():
    for bad in (0, -7):
        try:
            sum_of_divisors(bad)
        except ValueError:
            pass
        else:
            raise AssertionError(f"ожидался ValueError для n={bad}")


def test_analyze_profile():
    p = analyze(6)
    assert p.divisors == [1, 2, 3, 6]
    assert p.divisor_count == 4
    assert p.divisor_sum == 12
    assert p.is_perfect and not p.is_abundant and not p.is_deficient
    assert not p.prime
    assert p.classify() == "совершенное"

    assert analyze(7).classify() == "простое"
    assert analyze(1).classify() == "единица"
    assert analyze(12).classify() == "избыточное"  # 1+2+3+4+6=16 > 12
    assert analyze(10).classify() == "недостаточное"  # 1+2+5=8 < 10


def test_analyze_invalid_input():
    for bad in (0, -1):
        try:
            analyze(bad)
        except ValueError:
            pass
        else:
            raise AssertionError(f"ожидался ValueError для n={bad}")


def test_perfect_numbers_in_range():
    # совершенные числа до 10000: 6, 28, 496, 8128
    assert perfect_numbers_in_range(1, 10000) == [6, 28, 496, 8128]
    # перепутанный порядок границ должен работать так же
    assert perfect_numbers_in_range(10000, 1) == [6, 28, 496, 8128]
    assert perfect_numbers_in_range(7, 27) == []


def test_abundant_numbers_in_range():
    # первые избыточные числа: 12, 18, 20, 24, 30, 36, ...
    assert abundant_numbers_in_range(1, 40) == [12, 18, 20, 24, 30, 36, 40]
    assert abundant_numbers_in_range(40, 1) == [12, 18, 20, 24, 30, 36, 40]
    # ни одно простое не бывает избыточным
    for n in abundant_numbers_in_range(1, 200):
        assert not analyze(n).prime


def test_range_validation():
    for fn in (perfect_numbers_in_range, abundant_numbers_in_range):
        try:
            fn(0, 10)
        except ValueError:
            pass
        else:
            raise AssertionError(f"ожидался ValueError в {fn.__name__}")


if __name__ == "__main__":
    test_sum_of_divisors_known_values()
    test_sum_of_divisors_matches_brute_force()
    test_sum_of_divisors_invalid_input()
    test_analyze_profile()
    test_analyze_invalid_input()
    test_perfect_numbers_in_range()
    test_abundant_numbers_in_range()
    test_range_validation()
    print("Все тесты analyzer пройдены")

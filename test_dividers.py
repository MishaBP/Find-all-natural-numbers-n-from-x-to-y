"""Тесты для dividers.get_divisors и новых функций."""

import math
import random

from dividers import (
    divisor_count,
    get_divisors,
    is_perfect,
    prime_factorization,
    product_of_divisors,
)


def brute_force_divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def test_small_numbers():
    assert get_divisors(1) == [1]
    assert get_divisors(2) == [1, 2]
    assert get_divisors(6) == [1, 2, 3, 6]
    assert get_divisors(9) == [1, 3, 9]
    assert get_divisors(12) == [1, 2, 3, 4, 6, 12]


def test_matches_brute_force_random():
    rng = random.Random(42)
    for _ in range(200):
        n = rng.randint(1, 5000)
        assert get_divisors(n) == brute_force_divisors(n), f"n={n}"


def test_invalid_input():
    for bad in (0, -5):
        try:
            get_divisors(bad)
        except ValueError:
            pass
        else:
            raise AssertionError(f"ожидался ValueError для n={bad}")


def test_prime_factorization():
    assert prime_factorization(1) == []
    assert prime_factorization(12) == [2, 2, 3]
    assert prime_factorization(97) == [97]
    assert prime_factorization(360) == [2, 2, 2, 3, 3, 5]


def test_divisor_count():
    assert divisor_count(1) == 1
    assert divisor_count(6) == 4
    assert divisor_count(9) == 3
    assert divisor_count(12) == 6
    rng = random.Random(5)
    for _ in range(200):
        n = rng.randint(1, 5000)
        assert divisor_count(n) == len(get_divisors(n)), f"n={n}"


def test_is_perfect():
    assert is_perfect(6)
    assert is_perfect(28)
    assert is_perfect(496)
    assert not is_perfect(10)
    assert not is_perfect(1)
    try:
        is_perfect(0)
    except ValueError:
        pass
    else:
        raise AssertionError("ожидался ValueError для n=0")


def test_product_of_divisors_matches_direct():
    assert product_of_divisors(1) == 1
    assert product_of_divisors(6) == 36  # 1*2*3*6
    assert product_of_divisors(9) == 27  # 1*3*9 (нечётное tau — точный квадрат)
    rng = random.Random(11)
    for _ in range(300):
        n = rng.randint(1, 3000)
        assert product_of_divisors(n) == math.prod(get_divisors(n)), f"n={n}"


def test_product_of_divisors_invalid_input():
    try:
        product_of_divisors(-3)
    except ValueError:
        pass
    else:
        raise AssertionError("ожидался ValueError для n=-3")


if __name__ == "__main__":
    test_small_numbers()
    test_matches_brute_force_random()
    test_invalid_input()
    test_prime_factorization()
    test_divisor_count()
    test_is_perfect()
    test_product_of_divisors_matches_direct()
    test_product_of_divisors_invalid_input()
    print("Все тесты пройдены")

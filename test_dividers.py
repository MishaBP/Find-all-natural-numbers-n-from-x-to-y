"""Тесты для dividers.get_divisors."""

import random

from dividers import get_divisors, prime_factorization


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


if __name__ == "__main__":
    test_small_numbers()
    test_matches_brute_force_random()
    test_invalid_input()
    test_prime_factorization()
    print("Все тесты пройдены")

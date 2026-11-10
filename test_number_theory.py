"""Тесты для number_theory.py: НОД/НОК, простота, решето, Фибоначчи."""

import math
import random

from number_theory import (
    fibonacci,
    fibonacci_list,
    gcd,
    gcd_many,
    is_prime,
    lcm,
    lcm_many,
    sieve_of_eratosthenes,
)


def test_gcd_lcm_known_values():
    assert gcd(12, 18) == 6
    assert gcd(-12, 18) == 6
    assert gcd(0, 5) == 5
    assert gcd(0, 0) == 0
    assert lcm(4, 6) == 12
    assert lcm(7, 13) == 91
    assert lcm(0, 5) == 0
    assert lcm(-4, 6) == 12


def test_gcd_lcm_matches_stdlib():
    rng = random.Random(7)
    for _ in range(300):
        a, b = rng.randint(0, 10_000), rng.randint(0, 10_000)
        assert gcd(a, b) == math.gcd(a, b), f"a={a}, b={b}"
        assert lcm(a, b) == (0 if a == 0 or b == 0 else a * b // math.gcd(a, b))


def test_gcd_many_lcm_many():
    assert gcd_many(12, 18, 24) == 6
    assert lcm_many(2, 3, 4) == 12
    assert gcd_many(7) == 7
    assert lcm_many(0, 5) == 0
    try:
        gcd_many()
    except ValueError:
        pass
    else:
        raise AssertionError("ожидался ValueError для пустого списка")


def test_is_prime():
    known_primes = [2, 3, 5, 7, 11, 13, 97, 7919]
    known_composites = [0, 1, 4, 9, 25, 100, 7917, 7921]
    for p in known_primes:
        assert is_prime(p), f"{p} должно быть простым"
    for c in known_composites:
        assert not is_prime(c), f"{c} не должно быть простым"


def test_sieve_matches_naive():
    naive = [n for n in range(2, 500) if all(n % d for d in range(2, n))]
    assert sieve_of_eratosthenes(499) == naive
    assert sieve_of_eratosthenes(1) == []
    assert sieve_of_eratosthenes(2) == [2]
    # известные значения: 25 простых до 100, 168 простых до 1000
    assert len(sieve_of_eratosthenes(100)) == 25
    assert len(sieve_of_eratosthenes(1000)) == 168


def test_sieve_agrees_with_is_prime():
    primes = set(sieve_of_eratosthenes(2000))
    for n in range(2001):
        assert is_prime(n) == (n in primes), f"n={n}"


def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(10) == 55
    assert fibonacci(20) == 6765
    assert fibonacci_list(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert fibonacci_list(0) == []
    # рекуррентность F(n) = F(n-1) + F(n-2)
    seq = fibonacci_list(30)
    for i in range(2, 30):
        assert seq[i] == seq[i - 1] + seq[i - 2]


def test_fibonacci_invalid_input():
    for bad_fn, args in ((fibonacci, (-1,)), (fibonacci_list, (-3,))):
        try:
            bad_fn(*args)
        except ValueError:
            pass
        else:
            raise AssertionError(f"ожидался ValueError для {bad_fn.__name__}{args}")


if __name__ == "__main__":
    test_gcd_lcm_known_values()
    test_gcd_lcm_matches_stdlib()
    test_gcd_many_lcm_many()
    test_is_prime()
    test_sieve_matches_naive()
    test_sieve_agrees_with_is_prime()
    test_fibonacci()
    test_fibonacci_invalid_input()
    print("Все тесты number_theory пройдены")

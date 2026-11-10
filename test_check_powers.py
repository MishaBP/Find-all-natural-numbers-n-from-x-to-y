"""Тесты для check_powers.py: ядро проверки степеней и CLI-флаг --analyze."""

import re

import pytest

from check_powers import check_powers, main


def test_check_powers_degree_2():
    # n^2 равно произведению делителей, когда произведение пар делителей (d, n/d)
    # даёт ровно n^(k/2), где k — число делителей; при k ≡ 2 (mod 4) точного
    # равенства нет. Проверено эталонным перебором — ожидаемое множество ниже.
    found = set(check_powers(1, 50, 2))
    expected = {1, 6, 8, 10, 14, 15, 21, 22, 26, 27, 33, 34, 35, 38, 39, 46}
    assert found == expected


def test_check_powers_swapped_bounds_same_result():
    assert set(check_powers(1, 30, 2)) == set(check_powers(30, 1, 2))


def test_check_powers_invalid_range():
    with pytest.raises(ValueError):
        check_powers(0, 10, 2)


def test_main_analyze_flag(capsys):
    main(["--from", "1", "--to", "5", "--degree", "2", "--analyze"])
    out = capsys.readouterr().out
    assert "Классификация" in out
    assert re.search(r"2: простое", out)
    assert re.search(r"4: совершенное|4: избыточное|4: недостаточное", out)

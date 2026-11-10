# Числовая библиотека: делители, степени и анализ чисел

Небольшой проект: для каждого числа из диапазона `[от; до]` проверяет,
равно ли `n**степень` произведению всех натуральных делителей `n`,
плюс набор утилит теории чисел с тестами.

## Структура
- `check_powers.py` — главный скрипт (точка входа), поддерживает CLI-аргументы
- `dividers.py` — `get_divisors` O(√n), `sum_of_divisors` σ(n), `divisor_count` τ(n),
  `product_of_divisors` (точная целочисленная формула n^(τ/2)), `is_perfect`,
  `prime_factorization`
- `number_theory.py` — `gcd`/`lcm` (+ версии для многих чисел), `is_prime`,
  `sieve_of_eratosthenes`, `fibonacci`/`fibonacci_list`
- `analyzer.py` — профиль числа (`analyze` → `NumberProfile`: делители, суммы,
  тип) и поиск совершенных/избыточных чисел в диапазоне
- `test_*.py` — тесты (unit + property-based сравнение с brute-force)

## Запуск
Интерактивный ввод (по одному числу в строке: от, до, степень):
```
python check_powers.py
```
Через аргументы командной строки (плюс классификация каждого числа):
```
python check_powers.py --from 1 --to 50 --degree 2 --analyze
```

## Тесты
```
pytest            # все тесты
python test_dividers.py        # или без pytest
python test_number_theory.py
python test_analyzer.py
python test_check_powers.py
```

Примечание: в `pytest.ini` отключён автоплагин сторонней библиотеки `libtmux`
(он несовместим с pytest >= 8 и ломает запуск); к нашим тестам это отношения не имеет.

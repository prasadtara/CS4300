import pytest
from src.task3 import classify_number, first_n_primes, sum_1_to_100, is_prime

@pytest.mark.parametrize(
    "n, expected",
    [(-1, "negative"), (0, "zero"), (1, "positive"), (999, "positive")],
)
def test_classify_number(n, expected):
    assert classify_number(n) == expected

def test_first_10_primes():
    assert first_n_primes(10) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

@pytest.mark.parametrize("n, expected", [(0, False), (1, False), (2, True), (9, False), (29, True)])
def test_is_prime(n, expected):
    assert is_prime(n) is expected

def test_sum_1_to_100():
    assert sum_1_to_100() == 5050

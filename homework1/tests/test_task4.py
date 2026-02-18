import pytest
from src.task4 import calculate_discount

@pytest.mark.parametrize(
    "price, discount, expected",
    [(100, 15, 85.0), (200.0, 25, 150.0), (19.99, 20.0, 15.992), (0, 50, 0.0)],
)
def test_calculate_discount_numeric_types(price, discount, expected):
    assert calculate_discount(price, discount) == pytest.approx(expected)

@pytest.mark.parametrize("bad_price", [-1, -0.01])
def test_negative_price(bad_price):
    with pytest.raises(ValueError):
        calculate_discount(bad_price, 10)

@pytest.mark.parametrize("bad_discount", [-1, 101])
def test_bad_discount(bad_discount):
    with pytest.raises(ValueError):
        calculate_discount(10, bad_discount)

def test_type_error():
    with pytest.raises(TypeError):
        calculate_discount("100", 10)

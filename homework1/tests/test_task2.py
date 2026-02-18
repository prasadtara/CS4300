import pytest
from src.task2 import get_demo_values

@pytest.mark.parametrize(
    "index, expected_type",
    [(0, int), (1, float), (2, str), (3, bool)],
)
def test_task2_types(index, expected_type):
    values = get_demo_values()
    assert isinstance(values[index], expected_type)

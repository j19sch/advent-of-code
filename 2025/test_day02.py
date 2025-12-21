import pytest
from day02_01 import is_invalid
from day02_02 import is_more_invalid


@pytest.mark.parametrize(
    "input,expected",
    [
        ("55", True),
        ("56", False),
        ("6464", True),
        ("6564", False),
        ("123123", True),
        ("123223", False),
        ("12312", False),
    ],
)
def test_is_invalid(input, expected):
    assert is_invalid(input) == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        ("55", True),
        ("56", False),
        ("6464", True),
        ("6564", False),
        ("123123", True),
        ("123223", False),
        ("12312", False),
        ("12341234", True),
        ("1212121212", True),
        ("1111111", True),
    ],
)
def test_is_more_invalid(input, expected):
    assert is_more_invalid(input) == expected

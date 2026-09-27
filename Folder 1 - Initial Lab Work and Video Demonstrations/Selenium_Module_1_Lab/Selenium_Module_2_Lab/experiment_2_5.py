import pytest


@pytest.fixture
def number():
    return 10


def test_addition(number):
    assert number + 20 == 30


def test_multiplication(number):
    assert number * 2 == 20
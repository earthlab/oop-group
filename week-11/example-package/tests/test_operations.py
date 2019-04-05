""" Tests for the operations module. """

import pytest
import mathematics


@pytest.fixture
def some_str():
    return "The quick brown fox jumps the lazy dog."


@pytest.fixture(params=list(range(100)))
def x(request):
    return request.param


class TestAdd():
    def test_one_plus_one(self):
        res = mathematics.add(1, 1)
        assert res == 2

    def test_zero(self, x):
        res = mathematics.add(x, 0)
        assert res == x

    def test_unsupported_operand_add(self, some_str):
        with pytest.raises(TypeError, match="unsupported operand"):
            mathematics.add(1, some_str)


class TestMultiply():
    def test_mult_zero(self, x):
        res = mathematics.multiply(x, 0)
        assert res == 0

    def test_mult_string_by_one(self, some_str):
        assert some_str == mathematics.multiply(some_str, 1)

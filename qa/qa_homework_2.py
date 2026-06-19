import pytest

class SimpleMath:
    def square (self, x) :
        return x * x
    def cube (self, x) :
        return x * x * x


@pytest.fixture
def simple_math():
    return SimpleMath()

def test_square(simple_math):
    assert simple_math.square(2) == 4

def test_cube(simple_math):
    assert simple_math.cube(-3) == -27
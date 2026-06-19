import pytest

class SimpleMath:
    def square (self, x) :
        return x * x
    def cube (self, x) :
        return x * x * x


def test_square():
    simple_math = SimpleMath()
    assert simple_math.square(2) == 4

def test_cube():
    simple_math = SimpleMath()
    assert simple_math.cube(-3) == -27
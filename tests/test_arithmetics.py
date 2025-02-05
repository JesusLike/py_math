import mathlib.arithmetics as math
from pytest import approx, raises

def test_add_integers():
    assert math.add(0, 0) == 0
    assert math.add(5, 5) == 10
    assert math.add(-7, 7) == 0
    assert math.add(-9, -9) == -18
    assert math.add(14, 29) == 43
    assert math.add(-25, -44) == -69
    
def test_add_floats():
    assert math.add(0.5, 0.5) == approx(1)
    assert math.add(-1.2, 1.2) == approx(0)
    assert math.add(2.71, 3.14) == approx(5.85)
    assert math.add(-15.857956, -3.1415926) == approx(-18.9995486)
    assert math.add(-4.58, 10.96) == approx(6.38)
    assert math.add(-7.32, 1.11) == approx(-6.21)
    
def test_substract_integers():
    assert math.substract(0, 0) == 0
    
    assert math.substract(5, 5) == 0
    assert math.substract(6, 2) == 4
    assert math.substract(7, 12) == -5
    assert math.substract(14, -3) == 17
    
    assert math.substract(-4, -4) == 0
    assert math.substract(-16, -8) == -8
    assert math.substract(-25, -37) == 12
    assert math.substract(-9, 15) == -24
    
def test_multiply_integers():
    assert math.multiply(0, 0) == 0
    assert math.multiply(123, 0) == 0
    assert math.multiply(0, -234) == 0
    
    assert math.multiply(1, 345) == 345
    assert math.multiply(456, 1) == 456
    assert math.multiply(567, -1) == -567
    assert math.multiply(-1, 678) == -678
    
    assert math.multiply(23, 34) == 782
    assert math.multiply(-12, 11) == -132
    assert math.multiply(-30, -40) == 1200
    
def test_divide_by_zero():
    with raises(ZeroDivisionError):
        result = math.divide(1, 0)

def test_divide_integers():
    assert math.divide(0, 1) == 0
    assert math.divide(1234, 1) == 1234
    assert math.divide(2345, 2345) == 1
    assert math.divide(3456, -1) == -3456
    assert math.divide(4567, -4567) == -1
    
    assert math.divide(612, 4) == 153
    assert math.divide(18, 6) == 3
    
    assert math.divide(100, 8) == approx(12.5)
    assert math.divide(3, 12) == approx(0.25)
    assert math.divide(10, 6) == approx(1.66666667)
     
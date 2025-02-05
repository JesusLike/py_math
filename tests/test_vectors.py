from mathlib.vectors import Vector2
from pytest import approx

def test_vector_init():
    vector = Vector2(12, 34)
    
    assert vector.x() == 12
    assert vector.y() == 34

def test_vector_add():
    first = Vector2(2, 5)
    second = Vector2(-7, 12)
    
    result = first.add(second)
    
    assert result.x() == -5
    assert result.y() == 17
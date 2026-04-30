import pytest
from calculator import calculate_simple_interest, calculate_compound_interest, calculate_tax


def test_simple_interest_correct():
    assert calculate_simple_interest(1000, 5, 2) == pytest.approx(100.0)
    assert calculate_simple_interest(5000, 10, 3) == pytest.approx(1500.0)

def test_simple_interest_zero_values():
    assert calculate_simple_interest(0, 5, 2) == 0.0
    assert calculate_simple_interest(1000, 0, 2) == 0.0
    assert calculate_simple_interest(1000, 5, 0) == 0.0

def test_simple_interest_negative_values():
    with pytest.raises(ValueError, match="Аргументы должны быть неотрицательными"):
        calculate_simple_interest(-100, 5, 2)
    with pytest.raises(ValueError, match="Аргументы должны быть неотрицательными"):
        calculate_simple_interest(100, -5, 2)
    with pytest.raises(ValueError, match="Аргументы должны быть неотрицательными"):
        calculate_simple_interest(100, 5, -1)


def test_compound_interest_correct():
    assert calculate_compound_interest(1000, 5, 2) == pytest.approx(1102.5)
    assert calculate_compound_interest(1000, 5, 2, 4) == pytest.approx(1104.4861)

def test_compound_interest_zero_values():
    assert calculate_compound_interest(0, 5, 2) == 0.0
    assert calculate_compound_interest(1000, 0, 2) == pytest.approx(1000.0)
    assert calculate_compound_interest(1000, 5, 0) == pytest.approx(1000.0)

def test_compound_interest_invalid_values():
    with pytest.raises(ValueError):
        calculate_compound_interest(-100, 5, 2)
    with pytest.raises(ValueError):
        calculate_compound_interest(1000, 5, 2, n=0)
    with pytest.raises(ValueError):
        calculate_compound_interest(1000, 5, 2, n=-2)
    with pytest.raises(ValueError):
        calculate_compound_interest(1000, 5, 2, n=1.5)


def test_tax_correct():
    assert calculate_tax(1000, 20) == pytest.approx(200.0)
    assert calculate_tax(5000, 15) == pytest.approx(750.0)

def test_tax_zero_values():
    assert calculate_tax(0, 20) == 0.0
    assert calculate_tax(1000, 0) == 0.0

def test_tax_invalid_rate():
    with pytest.raises(ValueError, match="диапазоне от 0 до 100"):
        calculate_tax(1000, -5)
    with pytest.raises(ValueError, match="диапазоне от 0 до 100"):
        calculate_tax(1000, 101)
    with pytest.raises(ValueError, match="диапазоне от 0 до 100"):
        calculate_tax(1000, 150)

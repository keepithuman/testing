"""
Tests for the calculator package.
"""

import pytest
from calculator import Calculator
from calculator.operations import add, subtract, multiply, divide


class TestOperations:
    """Test the basic operations functions."""
    
    def test_add(self):
        """Test addition operation."""
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
        assert add(0, 0) == 0
        assert add(1.5, 2.5) == 4.0
    
    def test_subtract(self):
        """Test subtraction operation."""
        assert subtract(5, 3) == 2
        assert subtract(1, 1) == 0
        assert subtract(0, 5) == -5
        assert subtract(2.5, 1.5) == 1.0
    
    def test_multiply(self):
        """Test multiplication operation."""
        assert multiply(3, 4) == 12
        assert multiply(-2, 3) == -6
        assert multiply(0, 5) == 0
        assert multiply(2.5, 2) == 5.0
    
    def test_divide(self):
        """Test division operation."""
        assert divide(10, 2) == 5
        assert divide(7, 2) == 3.5
        assert divide(-6, 3) == -2
        assert divide(0, 5) == 0
    
    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)


class TestCalculator:
    """Test the Calculator class."""
    
    def test_calculator_init(self):
        """Test calculator initialization."""
        calc = Calculator()
        assert calc.get_history() == []
    
    def test_calculator_add(self):
        """Test calculator addition with history."""
        calc = Calculator()
        result = calc.add(2, 3)
        assert result == 5
        assert "2 + 3 = 5" in calc.get_history()
    
    def test_calculator_subtract(self):
        """Test calculator subtraction with history."""
        calc = Calculator()
        result = calc.subtract(5, 3)
        assert result == 2
        assert "5 - 3 = 2" in calc.get_history()
    
    def test_calculator_multiply(self):
        """Test calculator multiplication with history."""
        calc = Calculator()
        result = calc.multiply(3, 4)
        assert result == 12
        assert "3 * 4 = 12" in calc.get_history()
    
    def test_calculator_divide(self):
        """Test calculator division with history."""
        calc = Calculator()
        result = calc.divide(10, 2)
        assert result == 5.0
        assert "10 / 2 = 5.0" in calc.get_history()
    
    def test_calculator_divide_by_zero(self):
        """Test calculator division by zero."""
        calc = Calculator()
        with pytest.raises(ValueError):
            calc.divide(5, 0)
    
    def test_calculator_history(self):
        """Test calculator history functionality."""
        calc = Calculator()
        calc.add(1, 2)
        calc.subtract(5, 3)
        calc.multiply(2, 4)
        
        history = calc.get_history()
        assert len(history) == 3
        assert "1 + 2 = 3" in history
        assert "5 - 3 = 2" in history
        assert "2 * 4 = 8" in history
        
        calc.clear_history()

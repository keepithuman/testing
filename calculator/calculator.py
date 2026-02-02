"""
Calculator class that provides a convenient interface for mathematical operations.
"""

from .operations import add, subtract, multiply, divide


class Calculator:
    """A calculator class that performs basic mathematical operations."""
    
    def __init__(self):
        """Initialize the calculator."""
        self.history = []
    
    def add(self, a, b):
        """Add two numbers and store the operation in history."""
        result = add(a, b)
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """Subtract b from a and store the operation in history."""
        result = subtract(a, b)
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """Multiply two numbers and store the operation in history."""
        result = multiply(a, b)
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        """Divide a by b and store the operation in history."""
        result = divide(a, b)
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def get_history(self):
        """Return the calculation history."""
        return self.history.copy()
    
    def clear_history(self):
        """Clear the calculation history."""
        self.history.clear()

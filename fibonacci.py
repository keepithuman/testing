"""
Fibonacci number calculator module.

This module provides functions to calculate the nth Fibonacci number
using both iterative and recursive approaches.
"""


def fibonacci_iterative(n):
    """
    Calculate the nth Fibonacci number using an iterative approach.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)
        
    Returns:
        int: The nth Fibonacci number
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b


def fibonacci_recursive(n):
    """
    Calculate the nth Fibonacci number using a recursive approach.
    
    Note: This is less efficient for large n due to repeated calculations.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)
        
    Returns:
        int: The nth Fibonacci number
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    
    if n <= 1:
        return n
    
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Alias for the more efficient iterative version
fibonacci = fibonacci_iterative


if __name__ == "__main__":
    # Example usage
    print("First 10 Fibonacci numbers:")
    for i in range(10):
        print(f"F({i}) = {fibonacci(i)}")

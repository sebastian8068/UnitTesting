def sum(a: float, b: float) -> float:
    """
    >>> sum(6, 7)
    13

    >>> sum(10, -10)
    0
    """
    return a + b


def substract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    """
    >>> divide(1, 0)
    Traceback (most recent call last):
    ValueError: Cannot divide by zero

    >>> divide(4, 2)
    2.0

    >>> divide(3, 7)
    0.42857142857142855
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

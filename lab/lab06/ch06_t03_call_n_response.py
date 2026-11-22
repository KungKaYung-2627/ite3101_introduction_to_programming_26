def square(n: float) -> float:
    """Returns the square of a number."""
    squared = n ** 2
    print("%d squared is %d." % (n, squared))
    return squared


square(10)
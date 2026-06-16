def add(a, b):
    """Add two numbers. Currently has an off-by-one bug."""
    return a + b + 1  # BUG: should be a + b


def multiply(a, b):
    """Multiply two numbers. Currently has a bug."""
    return a * b + a  # BUG: should be a * b

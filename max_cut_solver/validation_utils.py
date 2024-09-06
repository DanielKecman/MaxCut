def validate_non_negative_number(value):
    if value < 0:
        raise ValueError(f"Expected non-negative value, but got <{value}>")


def validate_positive_number(value):
    if value <= 0:
        raise ValueError(f"Expected positive value, but got <{value}>")
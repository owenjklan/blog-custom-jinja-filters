from decimal import Decimal


def monetary_value_filter(value: Decimal) -> str:
    f1 = f"{value:.2f}"
    f2 = f"{value}"

    return max(f1, f2)

from numbers import Real

def calculate_discount(price, discount):
    """
    Calculate final price after applying a discount percentage.

    Accepts any numeric types (duck-typed) that behave like Real numbers.
    - price must be non-negative
    - discount is a percentage in [0, 100]
    """
    if not isinstance(price, Real) or not isinstance(discount, Real):
        raise TypeError("price and discount must be numeric")

    if price < 0:
        raise ValueError("price must be non-negative")

    if discount < 0 or discount > 100:
        raise ValueError("discount must be between 0 and 100")

    return price * (1 - (discount / 100))


def main() -> None:
    print(calculate_discount(100, 15))


if __name__ == "__main__":
    main()

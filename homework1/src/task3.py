def classify_number(n: int) -> str:
    """Return 'positive', 'negative', or 'zero'."""
    if n > 0:
        return "positive"
    if n < 0:
        return "negative"
    return "zero"


def is_prime(n: int) -> bool:
    """Return True if n is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def first_n_primes(count: int = 10) -> list[int]:
    """Return the first `count` prime numbers."""
    primes: list[int] = []
    candidate = 2
    while len(primes) < count:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return primes


def sum_1_to_100() -> int:
    """Compute the sum of 1..100 inclusive using a while loop."""
    total = 0
    i = 1
    while i <= 100:
        total += i
        i += 1
    return total


def main() -> None:
    print(classify_number(-3))
    print(first_n_primes(10))
    print(sum_1_to_100())


if __name__ == "__main__":
    main()

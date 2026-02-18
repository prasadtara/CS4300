def favorite_books():
    """Return a list of (title, author) tuples."""
    return [
        ("Dune", "Frank Herbert"),
        ("The Hobbit", "J.R.R. Tolkien"),
        ("1984", "George Orwell"),
        ("The Left Hand of Darkness", "Ursula K. Le Guin"),
        ("The Martian", "Andy Weir"),
    ]


def first_three_books(books: list[tuple[str, str]]):
    """Return first three books using list slicing."""
    return books[:3]


def student_database():
    """Return a dict mapping student names to student IDs."""
    return {
        "Ada Lovelace": "S001",
        "Alan Turing": "S002",
        "Grace Hopper": "S003",
    }


def main() -> None:
    books = favorite_books()
    print(first_three_books(books))
    print(student_database())


if __name__ == "__main__":
    main()

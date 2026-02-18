def get_demo_values():
    """Return one value of each required type: int, float, str, bool."""
    an_int = 42
    a_float = 3.5
    a_string = "cs4300"
    a_bool = True
    return an_int, a_float, a_string, a_bool


def main() -> None:
    an_int, a_float, a_string, a_bool = get_demo_values()
    print(an_int)
    print(a_float)
    print(a_string)
    print(a_bool)


if __name__ == "__main__":
    main()

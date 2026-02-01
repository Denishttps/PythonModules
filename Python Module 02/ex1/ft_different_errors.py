def garden_operations(action: str):
    if action == "value":
        int("str")
    elif action == "zero":
        10 / 0
    elif action == "file":
        with open("missing.txt") as _:
            pass
    elif action == "key":
        {}["missing\\_plant"]


def test_error_types():
    print("=== Garden Error Types Demo ===\n")

    print("Testing ValueError...")
    try:
        garden_operations("value")
    except ValueError as e:
        print(f"Caught {e.__class__.__name__}: {e}\n")

    print("Testing ZeroDivisionError...")
    try:
        garden_operations("zero")
    except ZeroDivisionError as e:
        print(f"Caught {e.__class__.__name__}: {e}\n")

    print("Testing FileNotFoundError...")
    try:
        garden_operations("file")
    except FileNotFoundError as e:
        print(f"Caught {e.__class__.__name__}: {e}\n")

    print("Testing KeyError...")
    try:
        garden_operations("key")
    except KeyError as e:
        print(f"Caught {e.__class__.__name__}: {e}\n")

    print("Testing multiple errors together...")
    try:
        # input("Write: value, zero, file, key: ")
        # for test all errors
        user_input = None
        garden_operations(user_input or "value")
    except (ValueError, KeyError, FileNotFoundError, ZeroDivisionError):
        print("Caught an error, but program continues!")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()

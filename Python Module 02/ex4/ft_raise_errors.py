def check_plant_health(
        plant_name: str,
        water_level: int,
        sunlight_hours: int
) -> None:
    try:
        water_level = int(water_level)
        sunlight_hours = int(sunlight_hours)
    except ValueError:
        raise ValueError("Water level and sunlight hours must be integers.")

    if not plant_name:
        raise ValueError("Plant name cannot be empty.")
    if water_level <= 0 or water_level > 10:
        raise ValueError("Water level must be between 1 and 10.")
    if sunlight_hours < 2 or sunlight_hours > 12:
        raise ValueError("Sunlight hours must be between 2 and 12.")

    print(
        f"{plant_name} is healthy with water level "
        f"{water_level} and {sunlight_hours} hours of sunlight."
    )


def test_plant_checks():
    print("="*50)
    print("=== Test plant health checks ===")

    print("Testing with valid parameters...")
    try:
        check_plant_health("Rose", 5, 6)
    except ValueError as e:
        print(e)

    print("\nTesting with empty plant name...")
    try:
        check_plant_health("", 5, 6)
    except ValueError as e:
        print(e.__class__.__name__ + ": " + str(e))

    print("\nTesting with invalid water level...")
    try:
        check_plant_health("Tulip", 0, 6)
    except ValueError as e:
        print(e.__class__.__name__ + ": " + str(e))

    print("\nTesting with invalid sunlight hours...")
    try:
        check_plant_health("Daisy", 5, 15)
    except ValueError as e:
        print(e.__class__.__name__ + ": " + str(e))

    print("\nTesting with non-integer water level...")
    try:
        check_plant_health("Lily", "five", 6)
    except ValueError as e:
        print(e.__class__.__name__ + ": " + str(e))

    print("\nTesting with non-integer sunlight hours...")
    try:
        check_plant_health("Orchid", 5, "six")
    except ValueError as e:
        print(e.__class__.__name__ + ": " + str(e))

    print("="*50)


if __name__ == "__main__":
    test_plant_checks()

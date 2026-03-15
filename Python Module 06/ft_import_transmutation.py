

def full_moodule_import():
    import alchemy

    fire = alchemy.elements.create_fire()
    print(f"alchemy.elements.create_fire(): {fire}")


def specific_function_import():
    from alchemy import create_water

    print(f"reate_water(): {create_water()}")


def aliased_import():
    from alchemy.potions import healing_potion as heal

    print(f"heal(): {heal()}")


def multiple_imports():
    from alchemy.potions import (
        create_earth,
        create_fire,
        strength_potion
    )

    print(f"create_earth(): {create_earth()}")
    print(f"create_fire(): {create_fire()}")
    print(f"strength_potion(): {strength_potion()}")


def main():
    print("=== Import Transmutation Mastery ===\n")

    print("Method 1 - Full module import:")
    full_moodule_import()

    print()

    print("Method 2 - Specific function import:")
    specific_function_import()

    print()

    print("Method 3 - Aliased import:")
    aliased_import()

    print()

    print("Method 4 - Multiple imports:")
    multiple_imports()

    print()

    print("All import transmutation methods mastered!")


if __name__ == "__main__":
    main()

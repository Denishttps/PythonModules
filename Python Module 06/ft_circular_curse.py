from alchemy.grimoire.validator import validate_ingredients
from alchemy.grimoire.spellbook import record_spell


def main():
    print("=== Circular Curse Breaking ===")
    print()

    print("Testing ingredient validation:")
    print(f'validate_ingredients("fire air"): {validate_ingredients("fire air")}')  # noqa
    print(f'validate_ingredients("dragon scales"): {validate_ingredients("dragon scales")}')  # noqa
    print()

    print("Testing spell recording with validation:")
    print(record_spell("Fireball", "fire air"))
    print(record_spell("Dark Magic", "shadow"))
    print()

    print("Testing late import technique:")
    print(record_spell("Lightning", "air"))
    print()

    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    main()

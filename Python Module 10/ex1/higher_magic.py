"""
Exercise 1: Higher Realm
Demonstrates higher-order functions and functions as first-class citizens.
"""

from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))

    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplified


def conditional_caster(
    condition: Callable, spell: Callable
) -> Callable:
    def cast(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return cast


def spell_sequence(spells: list[Callable]) -> Callable:
    def cast_all(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]

    return cast_all


def main() -> None:
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} damage"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    def lightning(target: str, power: int) -> str:
        return f"Lightning strikes {target} for {power} damage"

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 10)
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original: {fireball('Dragon', 10)}")
    print(f"Amplified: {mega_fireball('Dragon', 10)}")

    print("\nTesting conditional caster...")
    is_powerful = lambda target, power: power >= 50  # noqa: E731
    conditional_fire = conditional_caster(is_powerful, fireball)
    print(f"Low power: {conditional_fire('Goblin', 30)}")
    print(f"High power: {conditional_fire('Dragon', 100)}")

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal, lightning])
    results = sequence("Knight", 20)
    for r in results:
        print(f"  {r}")

    print("\ncallable() checks:")
    print(f"  fireball is callable: {callable(fireball)}")
    print(f"  42 is callable: {callable(42)}")


if __name__ == "__main__":
    main()

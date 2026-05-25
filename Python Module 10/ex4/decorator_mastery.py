"""
Exercise 4: Master's Tower
Demonstrates decorators, functools.wraps, and staticmethod.
"""

import functools
import inspect
import time
from collections.abc import Callable


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: object, **kwargs: object) -> object:
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: object, **kwargs: object) -> object:
            power = kwargs.get("power")
            if power is None:
                sig = inspect.signature(func)
                params = list(sig.parameters.keys())
                if "power" in params:
                    idx = params.index("power")
                    if idx < len(args):
                        power = args[idx]

            if power is not None and power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: object, **kwargs: object) -> object:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        f"Spell failed, retrying..."
                        f" (attempt {attempt}/{max_attempts})"
                    )
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return (
            len(name) >= 3
            and all(c.isalpha() or c == " " for c in name)
        )

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    result = fireball()
    print(f"Result: {result}")

    print("\nTesting retrying spell...")

    @retry_spell(max_attempts=3)
    def always_fails() -> str:
        raise RuntimeError("Spell unstable!")

    print(always_fails())

    attempt_count = {"n": 0}

    @retry_spell(max_attempts=3)
    def eventually_works() -> str:
        attempt_count["n"] += 1
        if attempt_count["n"] < 3:
            raise RuntimeError("Not ready yet!")
        return "Waaaaaaagh spelled !"

    print(eventually_works())

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("X"))
    print(guild.cast_spell("Lightning", power=15))
    print(guild.cast_spell("Fizzle", power=5))


if __name__ == "__main__":
    main()

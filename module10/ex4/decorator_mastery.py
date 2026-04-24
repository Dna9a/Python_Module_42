from functools import wraps
import time
from typing import Any, Callable

BLUE = "\033[44m\033[38;2;5;5;5m"
RST = "\033[0m"

"""Demonstrate decorators and static methods."""


def spell_timer(func: Callable) -> Callable:
    """Measure function execution time and print cast logs."""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable:
    """Validate power level before allowing spell execution."""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = kwargs.get("power")
            if power is None and args:
                last_arg = args[-1]
                power = last_arg if isinstance(last_arg, int) else None

            if power is None or power < min_power:
                return "Insufficient power for this spell"

            return func(*args, **kwargs)

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:
    """Retry a spell function when it raises an exception."""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            "Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )

            return "Spell casting failed after " f"{max_attempts} attempts"

        return wrapper

    return decorator


class MageGuild:
    """Represent a guild that validates names and casts spells."""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Return true when name has letters/spaces and length >= 3."""
        cleaned = name.strip()
        return len(cleaned) >= 3 and all(
            char.isalpha() or char.isspace() for char in cleaned
        )

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Cast a spell when power meets the required threshold."""
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    """Example timed spell."""
    time.sleep(0.1)
    return "Fireball cast!"


@retry_spell(3)
def unstable_spell() -> str:
    """Example spell that always fails to show retry behavior."""
    raise RuntimeError("Wild magic surge")


if __name__ == "__main__":
    print(f"{BLUE}Testing spell timer...{RST}")
    print(f"Result: {fireball()}")

    print(f"{BLUE}Testing retrying spell...{RST}")
    print(unstable_spell())

    print(f"{BLUE}Testing MageGuild...{RST}")
    print(MageGuild.validate_mage_name("Merlin"))
    print(MageGuild.validate_mage_name("X1"))
    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 7))

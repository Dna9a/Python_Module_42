"""Demonstrate reduce, partial, lru_cache, and singledispatch usage."""

from functools import lru_cache, partial, reduce, singledispatch
import operator
from typing import Any, Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    """Reduce spell powers with the selected operation."""
    if not spells:
        return 0

    operations: dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }

    if operation not in operations:
        raise ValueError("Unknown operation. Use: add, multiply, max, or min.")

    return reduce(operations[operation], spells)


def partial_enchanter(
    base_enchantment: Callable[[int, str, str], str],
) -> dict[str, Callable[[str], str]]:
    """Create specialized enchantments with pre-filled power and element."""
    return {
        "fire": partial(base_enchantment, 50, "fire"),
        "ice": partial(base_enchantment, 50, "ice"),
        "lightning": partial(base_enchantment, 50, "lightning"),
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Return the nth Fibonacci number with memoization."""
    if n < 0:
        raise ValueError("n must be >= 0")
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    """Return a single-dispatch spell handler."""

    @singledispatch
    def dispatch(spell: Any) -> str:
        return "Unknown spell type"

    @dispatch.register
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch.register
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatch.register
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatch


def enchant(power: int, element: str, target: str) -> str:
    """Base enchantment used for partial application demo."""
    return f"{element.title()} enchantment on {target} at {power} power"


if __name__ == "__main__":
    print("Testing spell reducer...")
    values = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(values, 'add')}")
    print(f"Product: {spell_reducer(values, 'multiply')}")
    print(f"Max: {spell_reducer(values, 'max')}")

    print("Testing partial enchanter...")
    enchanted = partial_enchanter(enchant)
    print(enchanted["fire"]("Dragon"))
    print(enchanted["ice"]("Golem"))
    print(enchanted["lightning"]("Wraith"))

    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print(f"Cache info: {memoized_fibonacci.cache_info()}")

    print("Testing spell dispatcher...")
    dispatch = spell_dispatcher()
    print(dispatch(42))
    print(dispatch("fireball"))
    print(dispatch(["burn", "freeze", "shock"]))
    print(dispatch({"mystery": True}))

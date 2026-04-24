"""Demonstrate higher-order functions with spell modifiers."""

from typing import Callable

Spell = Callable[[str, int], str]
Condition = Callable[[str, int], bool]
CombinedSpell = Callable[[str, int], tuple[str, str]]
SequenceSpell = Callable[[str, int], list[str]]


def spell_combiner(spell1: Spell, spell2: Spell) -> CombinedSpell:
    """Return a spell that executes both spells with the same arguments."""

    return lambda target, power: (
        spell1(target, power),
        spell2(target, power),
    )


def power_amplifier(base_spell: Spell, multiplier: int) -> Spell:
    """Return a spell that multiplies power before casting."""

    return lambda target, power: base_spell(target, power * multiplier)


def conditional_caster(condition: Condition, spell: Spell) -> Spell:
    """Return a spell that only casts when condition is true."""

    return lambda target, power: (
        spell(target, power) if condition(target, power) else "Spell fizzled"
    )


def spell_sequence(spells: list[Spell]) -> SequenceSpell:
    """Return a spell that executes all spells and gathers results."""

    return lambda target, power: [spell(target, power) for spell in spells]


def fireball(target: str, power: int) -> str:
    """Sample offensive spell."""

    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    """Sample restorative spell."""

    return f"Heal restores {target} for {power} HP"


def shield(target: str, power: int) -> str:
    """Sample defensive spell."""

    return f"Shield protects {target} with {power} armor"


def has_enough_power(_target: str, power: int) -> bool:
    """Condition used by conditional caster in the demo."""

    return power >= 8


if __name__ == "__main__":
    target_name = "Dragon"
    base_power = 10

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    first, second = combined(target_name, base_power)
    print(f"Combined spell result: {first}, {second}")

    print("Testing power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original: {base_power}, Amplified: {base_power * 3}")
    print(mega_fireball(target_name, base_power))

    print("Testing conditional caster...")
    safe_heal = conditional_caster(has_enough_power, heal)
    print(safe_heal(target_name, 4))
    print(safe_heal(target_name, 12))

    print("Testing spell sequence...")
    combo_chain = spell_sequence([fireball, shield, heal])
    print(combo_chain(target_name, base_power))

    print("Callable origin: typing.Callable")
    print(f"Is 'fireball' callable? {callable(fireball)}")

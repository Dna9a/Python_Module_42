from typing import Callable

BLUE = "\033[44m\033[38;2;5;5;5m"
RST = "\033[0m"


Spell = Callable[[str, int], str]
Condition = Callable[[str, int], bool]
CombinedSpell = Callable[[str, int], tuple[str, str]]
SequenceSpell = Callable[[str, int], list[str]]


def spell_combiner(spell1: Spell, spell2: Spell) -> CombinedSpell:
    return lambda target, power: (
        spell1(target, power),
        spell2(target, power),
    )


def power_amplifier(base_spell: Spell, multiplier: int) -> Spell:
    return lambda target, power: base_spell(target, power * multiplier)


def conditional_caster(condition: Condition, spell: Spell) -> Spell:
    return lambda target, power: (
        spell(target, power) if condition(target, power) else "Spell fizzled"
    )


def spell_sequence(spells: list[Spell]) -> SequenceSpell:
    return lambda target, power: [spell(target, power) for spell in spells]


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def shield(target: str, power: int) -> str:
    return f"Shield protects {target} with {power} armor"


def has_enough_power(_target: str, power: int) -> bool:
    return power >= 8


if __name__ == "__main__":
    target_name = "Dragon"
    base_power = 10

    print(f"{BLUE}Testing spell combiner...{RST}")
    combined = spell_combiner(fireball, heal)
    first, second = combined(target_name, base_power)
    print(f"Combined spell result: {first}, {second}")

    print(f"\n{BLUE}Testing power amplifier...{RST}")
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original: {base_power}, Amplified: {base_power * 3}")
    print(mega_fireball(target_name, base_power))

    print(f"\n{BLUE}Testing conditional caster...{RST}")
    safe_heal = conditional_caster(has_enough_power, heal)
    print(safe_heal(target_name, 4))
    print(safe_heal(target_name, 12))

    print(f"\n{BLUE}Testing spell sequence...{RST}")
    combo_chain = spell_sequence([fireball, shield, heal])
    print(combo_chain(target_name, base_power))

    print("Callable origin: typing.Callable")
    print(f"Is 'fireball' callable? {callable(fireball)}")

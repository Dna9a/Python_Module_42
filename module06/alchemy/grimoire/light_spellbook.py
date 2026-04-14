from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    validation_result = validate_ingredients(ingredients)
    keyword = validation_result.rsplit(": ", 1)[-1]
    if keyword == "VALID":
        return f"Spell recorded: {spell_name} ({ingredients} - VALID)"

    return f"Spell rejected: {spell_name} ({ingredients} - INVALID)"

from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = set(dark_spell_allowed_ingredients())
    parsed = [
        part.strip().lower()
        for part in ingredients.split(",")
        if part.strip()
    ]
    keyword = "VALID" if any(part in allowed for part in parsed) else "INVALID"
    return f"{ingredients} - {keyword}"

def validate_ingredients(ingredients: str) -> str:
    allowed_ingredients = {"earth", "air", "fire", "water"}
    parsed_ingredients = [
        ingredient.strip().lower()
        for ingredient in ingredients.split(",")
        if ingredient.strip()
    ]
    keyword = "VALID" if any(
        ingredient in allowed_ingredients
        for ingredient in parsed_ingredients
    ) else "INVALID"
    return f"{ingredients}: {keyword}"


def validate_light_ingredients(
    ingredients: list[str],
    allowed_ingredients: list[str],
) -> bool:
    if not ingredients:
        return False
    return all(ingredient in allowed_ingredients for ingredient in ingredients)

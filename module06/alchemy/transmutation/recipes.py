from elements import create_fire
from ..elements import create_air
from ..potion import strength_potion


def lead_to_gold():
    air = create_air()
    strength = strength_potion()
    fire = create_fire()

    return (
        "Recipe transmuting Lead to Gold: brew "
        f"'{air}' and "
        f"'{strength}' mixed with "
        f"'{fire}'"
    )

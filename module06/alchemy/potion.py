from alchemy.elements import create_air, create_earth
from elements import create_fire, create_water


air = create_air()
water = create_water()
fire = create_fire()
earth = create_earth()


def healing_potion():
    return f"Healing potion brewed with '{earth}' and '{air}'"


def strength_potion():
    return f"Strength potion brewed with '{fire}' and '{water}'"

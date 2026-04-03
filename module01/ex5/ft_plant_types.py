#!/Users/yoabied/.pyenv/versions/3.11.9/bin/python


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.__age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.__age} days old")

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.__age += 1


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self._is_blooming = False

    def bloom(self) -> None:
        self._is_blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._is_blooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.height:.1f}cm long and {self.trunk_diameter:.1f}cm wide."
        )


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, harvest_season: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self) -> None:
        super().grow()
        self.height += 1.3
        self.nutritional_value += 0.5

    def age(self) -> None:
        super().age()
        self.nutritional_value += 0.5

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {round(self.nutritional_value)}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()


"""

Authorized: super(), print(), range(), round()

The garden now needs to handle different types of plants: flowers, trees, and vegetables.
Each type has unique characteristics but inherits common plant features from its parent
category.
Requirements:
• Start with your Plant class from the previous exercise, which holds the common
features (name, height, and age)
• Create specialized types: Flower, Tree, and Vegetable
• Each specialized type should inherit the basic plant features
• Flower needs: a color attribute and ability to bloom()
• Tree needs: a trunk_diameter attribute and the ability to produce_shade()
• Vegetable needs: a harvest_season and a nutritional_value attributes
• When creating specialized plants, call the parent methods from inside your new
class using super(). It can be applied to any method, including __init__()
• A call to show() on a specialized class needs to print the standard Plant output
and the extra characteristics of your specialized plant. Your method override can
re-use the already existing code in the parent.
• Create at least one instance of each plant type; make the flower bloom; make the
nutritional value start from 0, then increase when the vegetable’s age() and grow()
methods are called.
Avoid duplicating common plant code across different specialized types.
• No need to validate the new attributes in the three new classes


Example:
$> python3 ft_plant_types.py
=== Garden Plant Types ===
=== Flower
Rose: 15.0cm, 10 days old
Color: red
Rose has not bloomed yet
[asking the rose to bloom]
Rose: 15.0cm, 10 days old
Color: red
Rose is blooming beautifully!
=== Tree
Oak: 200.0cm, 365 days old
Trunk diameter: 5.0cm
[asking the oak to produce shade]
Tree Oak now produces a shade of 200.0cm long and 5.0cm wide.
=== Vegetable
Tomato: 5.0cm, 10 days old
Harvest season: April
Nutritional value: 0
[make tomato grow and age for 20 days]
Tomato: 47.0cm, 30 days old
Harvest season: April
Nutritional value: 20

How are you handling the common features shared by all plant types?
It is advised to avoid repeating the same code in the different
classes to handle these common features.

"""

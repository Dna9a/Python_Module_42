#!/Users/yoabied/.pyenv/versions/3.11.9/bin/python


class Plant:
    class __Stats:
        def __init__(self) -> None:
            self.grow_count = 0
            self.age_count = 0
            self.show_count = 0

        def display(self) -> None:
            print(f"Stats: {self.grow_count} grow, {self.age_count} age, {self.show_count} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.__age = age
        self.__stats = Plant.__Stats()

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def show(self) -> None:
        self.__stats.show_count += 1
        print(f"{self.name}: {self.height:.1f}cm, {self.__age} days old")

    def grow(self) -> None:
        self.__stats.grow_count += 1
        self.height += 0.8

    def age(self) -> None:
        self.__stats.age_count += 1
        self.__age += 1

    def get_stats(self) -> None:
        self.__stats.display()


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
    class __TreeStats:
        def __init__(self) -> None:
            self.grow_count = 0
            self.age_count = 0
            self.show_count = 0
            self.shade_count = 0

        def display(self) -> None:
            print(f"Stats: {self.grow_count} grow, {self.age_count} age, {self.show_count} show")
            print(f"{self.shade_count} shade")

    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self._Tree__tree_stats = Tree.__TreeStats()

    def show(self) -> None:
        self._Tree__tree_stats.show_count += 1
        print(f"{self.name}: {self.height:.1f}cm, {self._Plant__age} days old")
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")

    def grow(self) -> None:
        self._Tree__tree_stats.grow_count += 1
        self.height += 0.8

    def age(self) -> None:
        self._Tree__tree_stats.age_count += 1
        self._Plant__age += 1

    def produce_shade(self) -> None:
        self._Tree__tree_stats.shade_count += 1
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.height:.1f}cm long and {self.trunk_diameter:.1f}cm wide."
        )

    def get_stats(self) -> None:
        self._Tree__tree_stats.display()


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")


def display_stats(plant: Plant) -> None:
    plant.get_stats()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[statistics for Rose]")
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    display_stats(rose)

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[statistics for Oak]")
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    display_stats(oak)

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    display_stats(sunflower)

    print("=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    print("[statistics for Unknown plant]")
    display_stats(anonymous)

from abc import ABC, abstractmethod
from typing import Any


class Creature(ABC):
	def __init__(self, name: str, creature_type: str) -> None:
		self.name = name
		self.creature_type = creature_type

	@abstractmethod
	def attack(self) -> str:
		raise NotImplementedError

	def describe(self) -> str:
		return f"{self.name} is a {self.creature_type} type Creature"


class Flameling(Creature):
	def __init__(self) -> None:
		super().__init__("Flameling", "Fire")

	def attack(self) -> str:
		return "Flameling uses Ember!"


class Pyrodon(Creature):
	def __init__(self) -> None:
		super().__init__("Pyrodon", "Fire/Flying")

	def attack(self) -> str:
		return "Pyrodon uses Flamethrower!"


class Aquabub(Creature):
	def __init__(self) -> None:
		super().__init__("Aquabub", "Water")

	def attack(self) -> str:
		return "Aquabub uses Water Gun!"


class Torragon(Creature):
	def __init__(self) -> None:
		super().__init__("Torragon", "Water")

	def attack(self) -> str:
		return "Torragon uses Hydro Pump!"


class CreatureFactory(ABC):
	@abstractmethod
	def create_base(self) -> Creature:
		raise NotImplementedError

	@abstractmethod
	def create_evolved(self) -> Creature:
		raise NotImplementedError


class FlameFactory(CreatureFactory):
	def create_base(self) -> Creature:
		return Flameling()

	def create_evolved(self) -> Creature:
		return Pyrodon()


class AquaFactory(CreatureFactory):
	def create_base(self) -> Creature:
		return Aquabub()

	def create_evolved(self) -> Creature:
		return Torragon()


def test_factory(factory: CreatureFactory) -> None:
	print("Testing factory")
	base = factory.create_base()
	evolved = factory.create_evolved()
	print(base.describe())
	print(base.attack())
	print(evolved.describe())
	print(evolved.attack())


def test_battle(first_factory: CreatureFactory, second_factory: CreatureFactory) -> None:
	print("Testing battle")
	first = first_factory.create_base()
	second = second_factory.create_base()
	print(first.describe())
	print("vs.")
	print(second.describe())
	print("fight!")
	print(first.attack())
	print(second.attack())


def main() -> None:
	flame_factory = FlameFactory()
	aqua_factory = AquaFactory()

	test_factory(flame_factory)
	test_factory(aqua_factory)
	test_battle(flame_factory, aqua_factory)


if __name__ == "__main__":
	main()

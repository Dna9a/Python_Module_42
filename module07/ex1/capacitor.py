from abc import ABC, abstractmethod

from module07.ex0.battle import Creature
from module07.ex0.battle import CreatureFactory


class HealCapability(ABC):
	@abstractmethod
	def heal(self) -> str:
		raise NotImplementedError


class TransformCapability(ABC):
	@abstractmethod
	def transform(self) -> str:
		raise NotImplementedError

	@abstractmethod
	def revert(self) -> str:
		raise NotImplementedError


class Sproutling(Creature, HealCapability):
	def __init__(self) -> None:
		super().__init__("Sproutling", "Grass")

	def attack(self) -> str:
		return "Sproutling uses Vine Whip!"

	def heal(self) -> str:
		return "Sproutling heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
	def __init__(self) -> None:
		super().__init__("Bloomelle", "Grass/Fairy")

	def attack(self) -> str:
		return "Bloomelle uses Petal Dance!"

	def heal(self) -> str:
		return "Bloomelle heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
	def __init__(self) -> None:
		super().__init__("Shiftling", "Normal")
		self._is_transformed = False

	def attack(self) -> str:
		if self._is_transformed:
			return "Shiftling performs a boosted strike!"
		return "Shiftling attacks normally."

	def transform(self) -> str:
		self._is_transformed = True
		return "Shiftling shifts into a sharper form!"

	def revert(self) -> str:
		self._is_transformed = False
		return "Shiftling returns to normal."


class Morphagon(Creature, TransformCapability):
	def __init__(self) -> None:
		super().__init__("Morphagon", "Normal/Dragon")
		self._is_transformed = False

	def attack(self) -> str:
		if self._is_transformed:
			return "Morphagon unleashes a devastating morph strike!"
		return "Morphagon attacks normally."

	def transform(self) -> str:
		self._is_transformed = True
		return "Morphagon morphs into a dragonic battle form!"

	def revert(self) -> str:
		self._is_transformed = False
		return "Morphagon stabilizes its form."


class HealingCreatureFactory(CreatureFactory):
	def create_base(self) -> Creature:
		return Sproutling()

	def create_evolved(self) -> Creature:
		return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
	def create_base(self) -> Creature:
		return Shiftling()

	def create_evolved(self) -> Creature:
		return Morphagon()


def _test_healing_family() -> None:
	print("Testing Creature with healing capability")
	factory = HealingCreatureFactory()
	base = factory.create_base()
	evolved = factory.create_evolved()

	print("base:")
	print(base.describe())
	print(base.attack())
	print(base.heal())

	print("evolved:")
	print(evolved.describe())
	print(evolved.attack())
	print(evolved.heal())


def _test_transform_family() -> None:
	print("Testing Creature with transform capability")
	factory = TransformCreatureFactory()
	base = factory.create_base()
	evolved = factory.create_evolved()

	print("base:")
	print(base.describe())
	print(base.attack())
	print(base.transform())
	print(base.attack())
	print(base.revert())

	print("evolved:")
	print(evolved.describe())
	print(evolved.attack())
	print(evolved.transform())
	print(evolved.attack())
	print(evolved.revert())


def main() -> None:
	_test_healing_family()
	_test_transform_family()


if __name__ == "__main__":
	main()
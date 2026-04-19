from abc import ABC, abstractmethod
from typing import List, Tuple

from module07.ex0.battle import AquaFactory
from module07.ex0.battle import Creature
from module07.ex0.battle import CreatureFactory
from module07.ex0.battle import FlameFactory
from module07.ex1.capacitor import HealCapability
from module07.ex1.capacitor import HealingCreatureFactory
from module07.ex1.capacitor import TransformCapability
from module07.ex1.capacitor import TransformCreatureFactory


class InvalidStrategyCreatureError(Exception):
	pass


class BattleStrategy(ABC):
	@abstractmethod
	def is_valid(self, creature: Creature) -> bool:
		raise NotImplementedError

	@abstractmethod
	def act(self, creature: Creature) -> List[str]:
		raise NotImplementedError


class NormalStrategy(BattleStrategy):
	def is_valid(self, creature: Creature) -> bool:
		return True

	def act(self, creature: Creature) -> List[str]:
		return [creature.attack()]


class AggressiveStrategy(BattleStrategy):
	def is_valid(self, creature: Creature) -> bool:
		return isinstance(creature, TransformCapability)

	def act(self, creature: Creature) -> List[str]:
		if not self.is_valid(creature):
			raise InvalidStrategyCreatureError(
				f"Invalid Creature '{creature.name}'for this aggressive strategy"
			)
		transformer = creature
		return [transformer.transform(), transformer.attack(), transformer.revert()]


class DefensiveStrategy(BattleStrategy):
	def is_valid(self, creature: Creature) -> bool:
		return isinstance(creature, HealCapability)

	def act(self, creature: Creature) -> List[str]:
		if not self.is_valid(creature):
			raise InvalidStrategyCreatureError(
				f"Invalid Creature '{creature.name}'for this defensive strategy"
			)
		healer = creature
		return [healer.attack(), healer.heal()]


Opponent = Tuple[CreatureFactory, BattleStrategy]


def battle(opponents: List[Opponent]) -> None:
	print("*** Tournament ***")
	print(f"{len(opponents)} opponents involved")

	for i in range(len(opponents)):
		for j in range(i + 1, len(opponents)):
			left_factory, left_strategy = opponents[i]
			right_factory, right_strategy = opponents[j]
			left_creature = left_factory.create_base()
			right_creature = right_factory.create_base()

			print("* Battle *")
			print(left_creature.describe())
			print("vs.")
			print(right_creature.describe())
			print("now fight!")

			try:
				for line in left_strategy.act(left_creature):
					print(line)
				for line in right_strategy.act(right_creature):
					print(line)
			except InvalidStrategyCreatureError as exc:
				print(f"Battle error, aborting tournament: {exc}")
				return


def main() -> None:
	normal = NormalStrategy()
	aggressive = AggressiveStrategy()
	defensive = DefensiveStrategy()

	flame_factory = FlameFactory()
	aqua_factory = AquaFactory()
	healing_factory = HealingCreatureFactory()
	transform_factory = TransformCreatureFactory()

	print("Tournament 0 (basic)")
	print("[ (Flameling+Normal), (Healing+Defensive) ]")
	battle([(flame_factory, normal), (healing_factory, defensive)])

	print("Tournament 1 (error)")
	print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
	battle([(flame_factory, aggressive), (healing_factory, defensive)])

	print("Tournament 2 (multiple)")
	print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
	battle([
		(aqua_factory, normal),
		(healing_factory, defensive),
		(transform_factory, aggressive),
	])


if __name__ == "__main__":
	main()
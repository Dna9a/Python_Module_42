from abc import ABC, abstractmethod
from typing import List
from typing import Tuple
from typing import cast

from ex0.bb import Creature
from ex0.bb import CreatureFactory
from ex1.cp import HealCapability
from ex1.cp import TransformCapability


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
                f"Invalid Creature '{creature.name}'for "
                f"this aggressive strategy"
            )
        return [
            cast(TransformCapability, creature).transform(),
            creature.attack(),
            cast(TransformCapability, creature).revert(),
        ]


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> List[str]:
        if not self.is_valid(creature):
            raise InvalidStrategyCreatureError(
                f"Invalid Creature '{creature.name}'for "
                f"this defensive strategy"
            )
        return [creature.attack(), cast(HealCapability, creature).heal()]


Opponent = Tuple[CreatureFactory, BattleStrategy]

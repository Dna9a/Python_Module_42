from abc import ABC, abstractmethod
from ex0.bb import Creature
from ex0.bb import CreatureFactory


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

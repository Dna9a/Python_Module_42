from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, creature_type: str) -> None:
        self.name = name
        self.creature_type = creature_type

    @abstractmethod
    def attack(self) -> str:
        raise NotImplementedError

    def describe(self) -> str:
        return f"{self.name} is a {self.creature_type} type Creature"


class Boukhncha(Creature):
    def __init__(self) -> None:
        super().__init__("Boukhncha", "Fire")

    def attack(self) -> str:
        return "Boukhncha uses Ember!"


class Bou3ou(Creature):
    def __init__(self) -> None:
        super().__init__("Bou3ou", "Fire/Flying")

    def attack(self) -> str:
        return "Bou3ou uses Flamethrower!"


class Boulolou(Creature):
    def __init__(self) -> None:
        super().__init__("Boulolou", "Water")

    def attack(self) -> str:
        return "Boulolou uses Water Gun!"


class Ja3bou9(Creature):
    def __init__(self) -> None:
        super().__init__("Ja3bou9", "Water")

    def attack(self) -> str:
        return "Ja3bou9  uses Hydro Pump!"


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        raise NotImplementedError

    @abstractmethod
    def create_evolved(self) -> Creature:
        raise NotImplementedError


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Boukhncha()

    def create_evolved(self) -> Creature:
        return Bou3ou()


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Boulolou()

    def create_evolved(self) -> Creature:
        return Ja3bou9()

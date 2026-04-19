
from typing import List
from typing import Tuple

from ex0 import AquaFactory
from ex0 import FlameFactory
from ex0.bb import CreatureFactory
from ex1 import HealingCreatureFactory
from ex1 import TransformCreatureFactory
from ex2 import AggressiveStrategy
from ex2 import BattleStrategy
from ex2 import DefensiveStrategy
from ex2 import InvalidStrategyCreatureError
from ex2 import NormalStrategy


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

            print("\n* Battle *")
            print(left_creature.describe())
            print(" vs.")
            print(right_creature.describe())
            print(" now fight!")

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
    print("")

    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([(flame_factory, aggressive), (healing_factory, defensive)])
    print("")

    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle(
        [
            (aqua_factory, normal),
            (healing_factory, defensive),
            (transform_factory, aggressive),
        ]
    )
    print("")


if __name__ == "__main__":
    main()

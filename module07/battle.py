from typing import Any
from ex0 import AquaFactory
from ex0 import FlameFactory


def test_factory(factory: Any) -> None:
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def test_battle(
    first_factory: Any, second_factory: Any
) -> None:
    print("Testing battle")
    first = first_factory.create_base()
    second = second_factory.create_base()
    print(first.describe())
    print("  vs.")
    print(second.describe())
    print("  fight!")
    print(first.attack())
    print(second.attack())


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    test_factory(flame_factory)
    print("")
    test_factory(aqua_factory)
    print("")
    test_battle(flame_factory, aqua_factory)
    print("")


if __name__ == "__main__":
    main()

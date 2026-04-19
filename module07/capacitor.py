from ex1 import HealingCreatureFactory
from ex1 import TransformCreatureFactory
from ex1.cp import HealCapability
from ex1.cp import TransformCapability
from typing import cast


def __evolve_justamsg() -> None:
    print("  evolved:")


def __base_justamsg() -> None:
    print("  base:")


def _test_healing_family() -> None:
    print("Testing Creature with healing capability")
    factory = HealingCreatureFactory()
    base = factory.create_base()
    evolved = factory.create_evolved()

    __base_justamsg()
    print(base.describe())
    print(base.attack())
    print(cast(HealCapability, base).heal())

    __evolve_justamsg()
    print(evolved.describe())
    print(evolved.attack())
    print(cast(HealCapability, evolved).heal())


def _test_transform_family() -> None:
    print("Testing Creature with transform capability")
    factory = TransformCreatureFactory()
    base = factory.create_base()
    evolved = factory.create_evolved()

    __base_justamsg()
    print(base.describe())
    print(base.attack())
    print(cast(TransformCapability, base).transform())
    print(base.attack())
    print(cast(TransformCapability, base).revert())

    __evolve_justamsg()
    print(evolved.describe())
    print(evolved.attack())
    print(cast(TransformCapability, evolved).transform())
    print(evolved.attack())
    print(cast(TransformCapability, evolved).revert())


def main() -> None:
    _test_healing_family()
    print("")
    _test_transform_family()
    print("")


if __name__ == "__main__":
    main()

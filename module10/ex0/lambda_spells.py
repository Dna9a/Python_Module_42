BG_RED = "\033[41m\033[38;2;5;5;5m"
FG_RED = "\033[31m"
BLUE = "\033[44m\033[38;2;5;5;5m"
FG_BLUE = "\033[34m"
BG_GREEN = "\033[42m\033[38;2;5;5;5m"
YELLOW = "\033[43m\033[38;2;5;5;5m"
CYN = "\033[46m\033[38;2;5;5;5m"
WHITE = "\033[48;2;255;255;255m\033[38;2;5;5;5m"
RST = "\033[0m"


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts,
        key=lambda artifact: artifact["power"],
        reverse=True,
    )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """Return mages whose power is greater than or equal to min_power."""
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """Return spells wrapped with asterisks using map and lambda."""
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    """Return max, min, and average mage power statistics."""
    if not mages:
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}

    return {
        "max_power": max(mages, key=lambda mage: mage["power"])["power"],
        "min_power": min(mages, key=lambda mage: mage["power"])["power"],
        "avg_power": round(
            sum(map(lambda mage: mage["power"], mages)) / len(mages),
            2,
        ),
    }


if __name__ == "__main__":
    artifacts_data = [
        {"name": "Sandalt Lwalida", "power": 9999},
        {"name": "Tarchet Lwalid", "power": 10000},
        {"name": "Darbatou Albo3bo3", "power": 5},
        {"name": "S9ateti Lbac", "power": 30},
    ]
    spells_data = ["fireball", "heal", "shield"]
    mages_data = [
        {"name": "Aeris", "power": 90, "element": "air"},
        {"name": "Pyra", "power": 78, "element": "fire"},
        {"name": "Neris", "power": 84, "element": "water"},
    ]

    print("-" * 45)
    print(f"|{BLUE} {'TESTING ARTIFACT SORTER':^43} {RST}|")
    print("-" * 45)
    ordered_artifacts = artifact_sorter(artifacts_data)
    first = ordered_artifacts[0]
    second = ordered_artifacts[1]
    print(
        f"{first['name']} ({first['power']} power) "
        f"comes before {second['name']} ({second['power']} power)"
    )

    print("\nTesting spell transformer...")
    print(" ".join(spell_transformer(spells_data)))

    print("Testing power filter...")
    print([mage["name"] for mage in power_filter(mages_data, 80)])

    print("Testing mage stats...")
    print(mage_stats(mages_data))

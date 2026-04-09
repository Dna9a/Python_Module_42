ACHIEVEMENTS_LIST = [
    "Crafting Genius",
    "World Savior",
    "Master Explorer",
    "Collector Supreme",
    "Untouchable",
    "Boss Slayer",
    "Strategist",
    "Speed Runner",
    "Survivor",
    "Treasure Hunter",
    "First Steps",
    "Sharp Mind",
    "Unstoppable",
    "Hidden Path Finder",
]


def gen_player_achievements(name):
    lista = {
        "Alice": {
            "Crafting Genius",
            "World Savior",
            "Master Explorer",
            "Collector Supreme",
            "Untouchable",
            "Boss Slayer",
        },
        "Bob": {
            "Crafting Genius",
            "Strategist",
            "World Savior",
            "Master Explorer",
            "Unstoppable",
            "Collector Supreme",
            "Untouchable",
        },
        "Charlie": {
            "Strategist",
            "Speed Runner",
            "Survivor",
            "Master Explorer",
            "Treasure Hunter",
            "First Steps",
            "Collector Supreme",
            "Untouchable",
            "Sharp Mind",
        },
        "Dylan": {
            "Strategist",
            "Speed Runner",
            "Unstoppable",
            "Untouchable",
            "Boss Slayer",
        },
    }
    return lista.get(name, set())


def main():
    print("=== Achievement Tracker System ===")

    player_names = ["Alice", "Bob", "Charlie", "Dylan"]
    players = {name: gen_player_achievements(name) for name in player_names}

    for name in player_names:
        print(f"Player {name}: {players[name]}")

    all_distinct = set().union(*players.values())
    print(f"All distinct achievements: {all_distinct}")

    common = set(players["Alice"]).intersection(
        *(players[name] for name in player_names[1:])
    )
    print(f"Common achievements: {common}")

    for name in player_names:
        achs = players[name]
        others_union = set().union(
            *(p_achs for p_name, p_achs in players.items() if p_name != name)
        )
        only_this_player = achs.difference(others_union)
        print(f"Only {name} has: {only_this_player}")

    for name in player_names:
        achs = players[name]
        missing = set(ACHIEVEMENTS_LIST).difference(achs)
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    main()

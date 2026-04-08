import random

ACHIEVEMENTS_LIST = [
    "First Steps",
    "Novice Explorer",
    "Data Miner",
    "Code Warrior",
    "Logic Master",
    "Bug Hunter",
    "Loop Specialist",
    "Function Guru",
    "List Wizard",
    "Tuple Traveler",
    "Set Sentinel",
    "Exception Expert",
    "Math Magician",
    "Command Commander",
    "Analytics Ace",
    "Quest Champion",
]


def gen_player_achievements():
    # Choose a random number of achievements (1 to total available)
    num_to_pick = random.randint(1, len(ACHIEVEMENTS_LIST))
    # Pick random achievements and return as a set
    return set(random.sample(ACHIEVEMENTS_LIST, num_to_pick))


def main():
    print("=== Achievement Tracker System ===")

    # Generate achievement sets for four players
    player_names = ["Player 1", "Player 2", "Player 3", "Player 4"]
    players = {name: gen_player_achievements() for name in player_names}

    # Track unique achievements among all the players
    all_unlocked = set().union(*players.values())
    print(f"Total Unique Achievements among all players: {len(all_unlocked)}")

    # Find achievements shared by all players
    shared_by_all = set(players["Player 1"]).intersection(
        *(players[name] for name in player_names[1:])
    )
    print(f"Achievements shared by ALL: {shared_by_all}")

    for name, achs in players.items():
        print(f"\n--- Analysis for {name} ---")

        # Others' achievements union
        others_achs = set().union(
            *(p_achs for p_name, p_achs in players.items() if p_name != name)
        )

        # Spot achievements no one else has
        unique_to_player = achs.difference(others_achs)
        print(f"Unique achievements: {unique_to_player}")

        # List missing achievements to have them all
        missing = set(ACHIEVEMENTS_LIST).difference(achs)
        print(f"Missing achievements: {missing}")


if __name__ == "__main__":
    main()

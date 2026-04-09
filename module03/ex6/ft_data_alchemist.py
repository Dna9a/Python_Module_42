import random

def main():
    print("=== Game Data Alchemist ===")
    initial_players = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    print(f"Initial list of players: {initial_players}")

    # All names capitalized
    capitalized_all = [name.capitalize() for name in initial_players]
    print(f"New list with all names capitalized: {capitalized_all}")

    # Only names that were already capitalized
    capitalized_only = [name for name in initial_players if name[0].isupper()]
    print(f"New list of capitalized names only: {capitalized_only}")

    # Score dictionary
    scores = {name: random.randint(1, 1000) for name in capitalized_all}
    print(f"Score dict: {scores}")

    average_score = sum(scores.values()) / len(scores)
    print(f"Score average is {average_score:.2f}")

    # High scores
    high_scores = {name: score for name, score in scores.items() if score > average_score}
    print(f"High scores: {high_scores}")

if __name__ == "__main__":
    main()

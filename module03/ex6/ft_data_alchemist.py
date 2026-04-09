import random

def main():
    print("=== Game Data Alchemist ===")
    
    # Initial list as provided in the instructions
    initial_players = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    print(f"Initial list of players: {initial_players}")

    # 1. List comprehension for all names capitalized
    capitalized_all = [name.capitalize() for name in initial_players]
    print(f"New list with all names capitalized: {capitalized_all}")

    # 2. List comprehension for names that were already capitalized
    capitalized_only = [name for name in initial_players if name[0].isupper()]
    print(f"New list of capitalized names only: {capitalized_only}")

    # 3. Dictionary comprehension for random scores (using the capitalized list)
    # Using a seed for reproducible example output logic if needed, but random is requested
    scores = {name: random.randint(1, 1000) for name in capitalized_all}
    print(f"Score dict: {scores}")

    # Calculate average
    average_score = sum(scores.values()) / len(scores)
    print(f"Score average is {average_score:.2f}")

    # 4. Dictionary comprehension for high scores (higher than average)
    high_scores = {name: score for name, score in scores.items() if score > average_score}
    print(f"High scores: {high_scores}")

if __name__ == "__main__":
    main()

# It is also possible to use comprehensions on sets.
# Each comprehension should be on a single line (unless it exceeds the
# line size).

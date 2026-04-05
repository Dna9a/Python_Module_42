import sys


def main():
    print("=== Player Score Analytics ===")

    if len(sys.argv) <= 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return

    scores = []

    for arg in sys.argv[1:]:
        try:
            score = int(arg)
            scores.append(score)
        except ValueError:
            print(f"Invalid parameter: '{arg}'")

    if not scores:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return

    total_players = len(scores)
    total_score = sum(scores)
    average_score = float(total_score / total_players)
    high_score = max(scores)
    low_score = min(scores)
    score_range = high_score - low_score

    print(f"Scores processed: {scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    main()

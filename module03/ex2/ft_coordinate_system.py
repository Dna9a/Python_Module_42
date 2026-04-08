import math


def get_player_pos(prompt):
    while True:
        try:
            user_input = input(prompt)
            # Split by comma and strip whitespace
            parts = [p.strip() for p in user_input.split(",")]

            if len(parts) != 3:
                print("Invalid syntax")
                continue

            # Try to convert each part to float
            coords = []
            for p in parts:
                try:
                    coords.append(float(p))
                except ValueError as e:
                    print(f"Error on parameter '{p}': {e}")
                    raise ValueError("Retry")  # Jump back to loop start

            return tuple(coords)

        except ValueError as e:
            if str(e) == "Retry":
                continue
            print(f"Invalid input: {e}")


def calculate_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2 + (p2[2] - p1[2]) ** 2)


def main():
    print("=== Game Coordinate System ===")

    # First set of coordinates
    print("Get a first set of coordinates")
    pos1 = get_player_pos("Enter new coordinates as floats in format 'x,y,z': ")
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")

    # Distance to center
    dist_to_center = calculate_distance(pos1, (0.0, 0.0, 0.0))
    print(f"Distance to center: {dist_to_center:.4f}")

    # Second set of coordinates
    print("Get a second set of coordinates")
    pos2 = get_player_pos("Enter new coordinates as floats in format 'x,y,z': ")

    # Distance between them
    dist_between = calculate_distance(pos1, pos2)
    print(f"Distance between the 2 sets of coordinates: {dist_between:.4f}")


if __name__ == "__main__":
    main()

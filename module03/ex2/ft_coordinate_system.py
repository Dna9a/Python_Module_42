import math


def get_player_pos(prompt):
    while True:
        try:
            user_input = input(prompt)
            parts = [p.strip() for p in user_input.split(",")]

            if len(parts) != 3:
                print("Invalid syntax")
                continue

            coords = []
            for p in parts:
                try:
                    coords.append(float(p))
                except ValueError as e:
                    print(f"Error on parameter '{p}': {e}")
                    raise ValueError("Retry")

            return tuple(coords)

        except ValueError as e:
            if str(e) == "Retry":
                continue
            print(f"Invalid input: {e}")


def calculate_distance(p1, p2):
    return math.sqrt(
        (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2 + (p2[2] - p1[2]) ** 2
        )


def main():
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")

    pause_flow = get_player_pos("Enter new coordinates as "
                                "floats in format 'x,y,z': ")

    print(f"Got a first tuple: {pause_flow}")
    print(f"It includes: X={pause_flow[0]}, "
          "Y={pause_flow[1]}, Z={pause_flow[2]}")

    dst_to_center = calculate_distance(pause_flow, (0.0, 0.0, 0.0))

    print(f"Distance to center: {dst_to_center:.4f}")
    print("\nGet a second set of coordinates")

    pos2 = get_player_pos("Enter new coordinates as "
                          "floats in format 'x,y,z': ")
    dist_between = calculate_distance(pause_flow, pos2)

    print(f"Distance between the 2 sets of coordinates: {dist_between:.4f}\n")


if __name__ == "__main__":
    main()

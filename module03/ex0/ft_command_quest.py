import sys


def arg() -> None:
    print("=== Command Quest ===")
    program_name = sys.argv[0]
    print(f"Program name: {program_name}")
    num_args = len(sys.argv) - 1
    if num_args == 0:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {num_args}")
        for i in range(1, len(sys.argv)):
            print(f"Argument {i}: {sys.argv[i]}")

    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    arg()

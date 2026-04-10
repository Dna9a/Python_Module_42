import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    file_name = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{file_name}'")

    try:
        with open(file_name, "r") as f:
            print("---\n")
            content = f.read()
            if content:
                print(content, end="" if content.endswith("\n") else "\n")
            print("\n---")
        print(f"File '{file_name}' closed.\n")
    except Exception as e:
        print(f"Error opening file '{file_name}': {e}")


if __name__ == "__main__":
    main()

import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return

    file_name = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_name}'")

    original_content = ""
    try:
        with open(file_name, "r") as f:
            print("---\n")
            original_content = f.read()
            if original_content:
                print(
                    original_content,
                    end="" if original_content.endswith("\n") else "\n",
                )
            print("---")
        print(f"File '{file_name}' closed.\n")
    except Exception as e:
        print(f"[STDERR] Error opening "
              f"file '{file_name}': {e}", file=sys.stderr)
        return

    lines = original_content.splitlines()
    transformed_content = "\n".join([f"{line}#" for line in lines])

    print("Transform data:")
    print("---")
    if transformed_content:
        print(transformed_content)
    print("---")

    print("Enter new file name (or empty): ", end="", flush=True)
    new_file_name_raw = sys.stdin.readline()
    if new_file_name_raw is None:
        new_file_name = ""
    else:
        new_file_name = new_file_name_raw.strip()

    if new_file_name:
        try:
            print(f"Saving data to '{new_file_name}'")
            with open(new_file_name, "w") as f:
                f.write(transformed_content)
            print(f"Data saved in file '{new_file_name}'.")
        except Exception as e:
            print(
                f"[STDERR] Error opening "
                f"file '{new_file_name}': {e}", file=sys.stderr
            )
            print("Data not saved.")
    else:
        print("Not saving data.")


if __name__ == "__main__":
    main()

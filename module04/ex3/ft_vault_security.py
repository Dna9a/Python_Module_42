def secure_archive(
    file_name: str, action: str = "read", content: str = ""
) -> tuple[bool, str]:
    try:
        if action == "write":
            with open(file_name, "w") as f:
                f.write(content)
            return (True, "Content successfully written to file")
        else:
            with open(file_name, "r") as f:
                data = f.read()
            return (True, data)
    except OSError as e:
        return (
            False,
            f"[{e.errno}] {e.strerror}: '{file_name}'",
        )
    except Exception as e:
        return (
            False,
            str(e),
        )


def main():
    print("=== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/shadow"))

    temp_file = "vault_temp.txt"
    example_content = (
        "[FRAGMENT 001] Digital preservation protocols established 2087\n"
        "[FRAGMENT 002] Knowledge must survive the entropy wars\n"
        "[FRAGMENT 003] Every byte saved is a victory against oblivion\n"
    )
    with open(temp_file, "w") as f:
        f.write(example_content)

    print("\nUsing 'secure_archive' to read from a regular file:")
    result = secure_archive(temp_file)
    print(result)

    print("Using 'secure_archive' to write previous content to a new file:")
    if result[0]:
        print(secure_archive("vault_ba"
                             "ckup.txt", action="write", content=result[1]))


if __name__ == "__main__":
    main()

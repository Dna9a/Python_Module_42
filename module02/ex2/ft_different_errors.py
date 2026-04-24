def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        2026 / 0
    elif operation_number == 2:
        with open("/non/existent/file", "r"):
            pass
    elif operation_number == 3:
        raise TypeError("Cannot add str and int")
    else:
        pass


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    for operation_num in range(5):
        print(f"Testing operation {operation_num}...")
        try:
            garden_operations(operation_num)
            print("Operation completed successfully")
        except (ValueError, ZeroDivisionError,
                FileNotFoundError, TypeError) as error:
            print(f"Caught {type(error).__name__}: {error}")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()

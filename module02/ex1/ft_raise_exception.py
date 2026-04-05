def input_temperature(temp_str: str) -> int:
    tmp_int = int(temp_str)
    if tmp_int < 0:
        raise ValueError(f"{tmp_int}°C is too cold for plants (min 0°C)")
    elif tmp_int > 40:
        raise ValueError(f"{tmp_int}°C is too hot for plants (max 40°C)")
    return tmp_int


def test_temperature() -> None:
    print("=== Garden Temperature ===")

    for temp_str in ("25", "abc", "500", "-50"):
        print(f"\nInput data is '{temp_str}'")
        try:
            temperature = input_temperature(temp_str)
            print(f"Temperature is now {temperature}°C")
        except ValueError as error:
            print(f"Caught input_temperature error: {error}")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()

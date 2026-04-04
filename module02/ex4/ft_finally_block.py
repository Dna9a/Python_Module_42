class PlantError(Exception):
    pass


def water_plant(plant_name: str) -> None:
    if not plant_name[:1].isupper():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")

    print("Testing valid plants...")
    print("Opening watering system")
    try:
        for plant_name in ("Tomato", "Lettuce", "Carrots"):
            water_plant(plant_name)
    finally:
        print("Closing watering system\n")

    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        for plant_name in ("Tomato", "lettuce", "Carrots"):
            water_plant(plant_name)
    except PlantError as error:
        print(f"Caught PlantError: {error}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system\n")

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()

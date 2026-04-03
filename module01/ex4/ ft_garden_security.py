#!/Users/yoabied/.pyenv/versions/3.11.9/bin/python


class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name = name
        self._height = 0.0
        self._age = 0

        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = float(height)

        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            self._age = 0
        else:
            self._age = age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = float(height)

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age

    def show(self) -> None:
        print(f"Plant created: {self._name}: {self._height}cm, {self._age} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = Plant("Rose", 15, 10)
    plant.show()
    plant.set_height(25)
    print("Height updated: 25cm")
    plant.set_age(30)
    print("Age updated: 30 days")
    plant.set_height(-5)
    plant.set_age(-10)
    print(
        f"Current state: {plant._name}: {plant.get_height()}cm, {plant.get_age()} days old"
    )

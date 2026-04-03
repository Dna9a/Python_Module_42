#!/Users/yoabied/.pyenv/versions/3.11.9/bin/python


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.__age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.__age} days old")

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.__age += 1


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")

    rose = Plant(
        "Rose",
        24.2,
        29
    )

    initial_height: float = rose.height
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age()
        rose.show()
    diff: float = rose.height - initial_height
    total_growth: float = round(diff, 2)
    print(f"Growth this week: {total_growth}cm")

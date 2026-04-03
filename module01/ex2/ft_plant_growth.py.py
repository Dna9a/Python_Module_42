#!/Users/yoabied/.pyenv/versions/3.11.9/bin/python


class Plant:
    def __init__(self) -> None:
        self.name: str = ""
        self.height: float = 0.0
        self.days_old: int = 0
        self.growth_rate: float = 0.8

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.height}cm," f" {self.days_old} days old")

    def grow(self) -> None:
        self.height = round(self.height + self.growth_rate, 1)

    def age(self) -> None:
        self.days_old += 1


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")

    rose = Plant()
    rose.name = "rose"
    rose.height = 25.0
    rose.days_old = 30
    rose.growth_rate = 0.8

    initial_height: float = rose.height

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.show()
        rose.grow()
        rose.age()

    total_growth: float = round(rose.height - initial_height, 1)
    print(f"Growth this week: {int(total_growth)}cm")

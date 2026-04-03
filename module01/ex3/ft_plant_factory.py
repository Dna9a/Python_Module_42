#!/Users/yoabied/.pyenv/versions/3.11.9/bin/python


class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"Created: {self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    rose = Plant("Rose", 25.0, 30)
    oak = Plant("Oak", 200.0, 365)
    cactus = Plant("Cactus", 5.0, 90)
    sunflower = Plant("Sunflower", 80.0, 45)
    fern = Plant("Fern", 15.0, 120)

    rose.show()
    oak.show()
    cactus.show()
    sunflower.show()
    fern.show()

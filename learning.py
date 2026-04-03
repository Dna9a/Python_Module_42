class Bro:
    def __init__(self, name: str, height: float, age: int, skin_color: bool) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.skin_color = skin_color

    def printit(self) -> None:
        print(f"{self.name}: {self.height}cm,")
        print(f"{self.age} yo,\n{self.skin_color} 👉🏿👈🏿 a7m")


if __name__ == "__main__":
    print("=== This is My Brother ===")
    hamid = Bro("Mohamed", 177.85, 24, False)
    hamid.printit()

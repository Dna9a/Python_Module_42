#!/Users/yoabied/.pyenv/versions/3.11.9/bin/python

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")






'''
=== Plant Factory Output ===
Created: Rose: 25.0cm, 30 days old
Created: Oak: 200.0cm, 365 days old
Created: Cactus: 5.0cm, 90 days old
Created: Sunflower: 80.0cm, 45 days old
Created: Fern: 15.0cm, 120 days old
'''
